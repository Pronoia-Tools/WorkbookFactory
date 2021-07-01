export default function ({ app, redirect }) {
  // if user not authenticated
  if (!app.store.state.auth.isLoggedIn) {
    return redirect('/login')
  }

  console.log(123, app.store.state.auth.isLoggedIn)
  // app.router.beforeResolve((to, from, next) => {
  //   if (app.store.state.auth.loginStatus) {
  //     next('/resource')
  //   } else {
  //     next()
  //   }
  // })
}
