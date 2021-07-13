export default function ({ app, redirect }) {
  // if user not authenticated
  // console.log('app.store', app.store.state.auth, { appp: app.$cookies })
  const cookies = app.$cookies
  const vuex = cookies.get('vuex')
  const { isLoggedIn } = vuex?.auth ?? {}

  if (process.server && !isLoggedIn) {
    return redirect('/login')
  }
}
