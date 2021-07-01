// import * as Cookies from 'js-cookie'
import { jwtDecrypt } from '../../shared/jwt.js'

const state = () => ({
  authData: {
    token: '',
    refreshToken: '',
    tokenExp: '',
    email: '',
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
    console.log(state.authData)
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
    document.cookie = 'access_token=' + response.access
    document.cookie = 'refresh_token=' + response.refresh

    const jwtDecodedValue = jwtDecrypt(response.access)
    const newTokenData = {
      token: response.access,
      refreshToken: response.refresh,
      tokenExp: jwtDecodedValue.exp,
      email: jwtDecodedValue.email,
    }

    state.authData = newTokenData
  },

  setLoginStatus(state, value) {
    console.log('🚀 ~ file: index.js ~ line 64 ~ setLoginStatus ~ state', state)
    state.isLoggedIn = value
  },

  removeTokenData() {
    document.cookie = 'access_token' + '=; Max-Age=0'
    document.cookie = 'refresh_token' + '=; Max-Age=0'
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
