import Cookies from 'js-cookie'
import { jwtDecrypt } from '../../shared/jwt.js'

const state = () => ({
  authData: {
    token: '',
    refreshToken: '',
    tokenExp: '',
  },
  isLoggedIn: false,
})

const getters = {
  getLoginStatus(state) {
    return state.isLoggedIn
  },
  getAuthData(state) {
    return state.authData
  },
  isTokenActive(state) {
    console.log(1, state.authData)
  },
}

const actions = {
  async login({ commit }, payload) {
    const response = await this.$axios
      .$post('/api/token/', payload)
      .catch((error) => {
        console.log(error)
      })

    if (response) {
      await commit('saveTokenData', response)
      await commit('setLoginStatus', true)
    } else {
      await commit('setLoginStatus', false)
    }
  },

  async logout({ commit }) {
    await commit('removeTokenData')
    await commit('setLoginStatus', false)
  },
}

const mutations = {
  saveTokenData(state, response) {
    Cookies.set('access_token', response.access)
    Cookies.set('refresh_token', response.refresh)

    const jwtDecodedValue = jwtDecrypt(response.access)
    const newTokenData = {
      token: response.access,
      refreshToken: response.refresh,
      tokenExp: jwtDecodedValue.exp,
    }

    state.authData = newTokenData
  },

  setLoginStatus(state, value) {
    state.isLoggedIn = value
  },

  removeTokenData() {
    // document.cookie = 'access_token' + '=; Max-Age=0'
    // document.cookie = 'refresh_token' + '=; Max-Age=0'
    Cookies.remove('access_token')
    Cookies.remove('refresh_token')
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
