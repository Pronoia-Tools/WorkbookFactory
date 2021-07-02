<template>
  <div
    class="
      min-h-screen
      flex
      items-center
      justify-center
      bg-gray-50
      py-12
      px-4
      sm:px-6
      lg:px-8
    "
  >
    <div class="max-w-md w-full space-y-8">
      <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
        Sign in to your account
      </h2>

      <form class="mt-8 space-y-6" method="POST">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm -space-y-px">
          <div class="mb-6">
            <label for="email-address" class="sr-only">Email address</label>
            <input
              id="email-address"
              v-model="email"
              name="email"
              type="email"
              autocomplete="email"
              required
              class="
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-t-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="Email address"
              :class="{ 'is-invalid': $v.email.$error }"
            />
            <div v-if="$v.email.$error" class="invalid-feedback">
              <span v-if="!$v.email.required">Email is required</span>
              <span v-if="!$v.email.email">Email is invalid</span>
            </div>
          </div>

          <div>
            <label for="password" class="sr-only">Password</label>
            <input
              id="password"
              v-model="password"
              name="password"
              type="password"
              autocomplete="current-password"
              required
              class="
                appearance-none
                rounded-none
                relative
                block
                w-full
                px-3
                py-2
                border border-gray-300
                placeholder-gray-500
                text-gray-900
                rounded-b-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="Password"
              :class="{ 'is-invalid': $v.password.$error }"
            />
            <div v-if="$v.password.$error" class="invalid-feedback">
              <span v-if="!$v.password.required">Password is required</span>
              <span v-if="!$v.password.minLength"
                >Password must be at least 6 characters</span
              >
            </div>
          </div>
        </div>

        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <input
              id="remember_me"
              name="remember_me"
              type="checkbox"
              class="
                h-4
                w-4
                text-indigo-600
                focus:ring-indigo-500
                border-gray-300
                rounded
              "
            />
            <label for="remember_me" class="ml-2 block text-sm text-gray-900">
              Remember me
            </label>
          </div>

          <div class="text-sm">
            <a
              href="#"
              class="font-medium text-indigo-600 hover:text-indigo-500"
            >
              Forgot your password?
            </a>
          </div>
        </div>

        <div>
          <button
            type="button"
            class="
              group
              relative
              w-full
              flex
              justify-center
              py-2
              px-4
              border border-transparent
              text-sm
              font-medium
              rounded-md
              text-white
              bg-indigo-600
              hover:bg-indigo-700
              focus:outline-none
              focus:ring-2
              focus:ring-offset-2
              focus:ring-indigo-500
            "
            @click="login()"
          >
            <span class="absolute left-0 inset-y-0 flex items-center pl-3">
              <!-- Heroicon name: solid/lock-closed -->
              <svg
                class="h-5 w-5 text-indigo-500 group-hover:text-indigo-400"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
                fill="currentColor"
                aria-hidden="true"
              >
                <path
                  fill-rule="evenodd"
                  d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z"
                  clip-rule="evenodd"
                />
              </svg>
            </span>
            Sign in
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import { validationMixin } from 'vuelidate'
import { required, email, minLength } from 'vuelidate/lib/validators'

export default {
  mixins: [validationMixin],
  data() {
    return {
      email: '',
      password: '',
    }
  },

  validations: {
    email: {
      required,
      email,
    },
    password: { required, minLength: minLength(6) },
  },

  computed: {
    ...mapGetters('auth', {
      getterLoginStatus: 'getLoginStatus',
    }),
  },

  methods: {
    ...mapActions('auth', {
      actionLogin: 'login',
    }),
    async login() {
      // stop here if form is invalid
      this.$v.$touch()
      if (this.$v.$invalid) {
        return
      }

      await this.actionLogin({
        email: this.email,
        password: this.password,
      })

      if (this.getterLoginStatus) {
        this.$toast({
          title: 'Success',
          description: "You're logged in successfully.",
          status: 'success',
          duration: 2000,
          position: 'top-right',
        })
        this.$router.push('/')
      } else {
        this.$toast({
          title: 'Failed',
          description: 'Please recheck your email or password.',
          status: 'error',
          duration: 2000,
          position: 'top-right',
        })
        this.$router.push('/login')
      }
    },
  },
}
</script>

<style scoped>
.invalid-feedback {
  color: red;
}
</style>
