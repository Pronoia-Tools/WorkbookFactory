export default function ({
  $axios,
  __isRetryRequest,
  store,
  app,
  redirect,
  payload,
  next,
}) {
  $axios.onRequest((config) => {
    if (app.$cookies.get('access_token') && app.$cookies.get('refresh_token')) {
      config.headers.common.Authorization = `Bearer ${app.$cookies.get(
        'access_token'
      )}`
    }
  })

  $axios.onResponseError((err) => {
    const code = parseInt(err.response && err.response.status)

    const originalRequest = err.config
    if (code === 401) {
      originalRequest.__isRetryRequest = true

      const token = app.$cookies.get('refresh_token')

      return new Promise((resolve, reject) => {
        $axios
          .post(`/api/token/refresh/`, {
            refresh_token: token,
          })
          .then((response) => {
            if (response.status === 200) {
              app.$cookies.set('access_token', response.data.access_token)
              app.$cookies.set('refresh_token', response.data.refresh_token)
              originalRequest.headers.Authorization = `Bearer ${response.data.access_token}`
            }
            resolve(response)
          })
          .catch((error) => {
            reject(error)
          })
      })
        .then((res) => {
          return $axios(originalRequest)
        })
        .catch((e) => {
          app.router.push('/login')
        })
    }
  })
}
