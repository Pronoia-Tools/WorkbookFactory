import VuexPersistence from 'vuex-persist'
import Cookies from 'js-cookie'

export default ({ store, req }) => {
  new VuexPersistence({
    key: 'vuex',
    /* your options */
    storage: {
      getItem: (key) => {
        return Cookies.getJSON(key)
      },
      setItem: (key, state) => {
        return Cookies.set(key, state, {
          expires: 3,
        })
      },
    },
  }).plugin(store)
}
