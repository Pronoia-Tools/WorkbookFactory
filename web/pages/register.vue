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
        Register your account
      </h2>

      <form class="mt-8 space-y-6" method="POST">
        <input type="hidden" name="remember" value="true" />
        <div class="rounded-md shadow-sm">
          <!-- user name -->
          <div class="mb-6">
            <label for="user-name" class="sr-only">User Name</label>
            <input
              id="user-name"
              v-model="userName"
              name="user-name"
              type="text"
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
                rounded-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="User name"
              :class="{ 'is-invalid': $v.userName.$error }"
            />
            <div v-if="$v.userName.$error" class="invalid-feedback">
              <span v-if="!$v.userName.required">User name is required</span>
              <span v-if="!$v.userName.userName">User name is invalid</span>
            </div>
          </div>
          <!-- first name -->
          <div class="mb-6">
            <label for="first-name" class="sr-only">First Name</label>
            <input
              id="first-name"
              v-model="firstName"
              name="first-name"
              type="text"
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
                rounded-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="First name"
              :class="{ 'is-invalid': $v.firstName.$error }"
            />
            <div v-if="$v.firstName.$error" class="invalid-feedback">
              <span v-if="!$v.firstName.required">First name is required</span>
            </div>
          </div>
          <!-- last name -->
          <div class="mb-6">
            <label for="last-name" class="sr-only">Last name</label>
            <input
              id="last-name"
              v-model="lastName"
              name="last-name"
              type="text"
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
                rounded-md
                focus:outline-none
                focus:ring-indigo-500
                focus:border-indigo-500
                focus:z-10
                sm:text-sm
              "
              placeholder="Last name"
              :class="{ 'is-invalid': $v.lastName.$error }"
            />
            <div v-if="$v.lastName.$error" class="invalid-feedback">
              <span v-if="!$v.lastName.required">lastName is required</span>
            </div>
          </div>
          <!-- email -->
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
                rounded-md
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
          <!-- password -->
          <div class="mb-6">
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
                rounded-md
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
          <!-- checkbox -->
          <div class="mb-6 flex">
            <!-- is_active -->
            <div class="flex items-center mr-10">
              <input
                id="is-active"
                v-model="isActive"
                name="is-active"
                type="checkbox"
                class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 rounded"
              />
              <label for="is-active" class="ml-2 block text-sm text-gray-900">
                Active
              </label>
            </div>
            <!-- is_staff -->
            <div class="flex items-center">
              <input
                id="is-staff"
                v-model="isStaff"
                name="is-staff"
                type="checkbox"
                class="h-4 w-4 text-indigo-600 focus:ring-indigo-500 rounded"
              />
              <label for="is-staff" class="ml-2 block text-sm text-gray-900">
                Staff
              </label>
            </div>
          </div>
        </div>

        <div class="text-sm">
          <nuxt-link
            to="/login"
            class="font-medium text-indigo-600 hover:text-indigo-500"
          >
            Already have an account?
          </nuxt-link>
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
            @click="registerUser()"
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
            Register
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { validationMixin } from 'vuelidate'
import { required, email, minLength } from 'vuelidate/lib/validators'

export default {
  mixins: [validationMixin],
  data() {
    return {
      userName: '',
      firstName: '',
      lastName: '',
      email: '',
      password: '',
      isActive: false,
      isStaff: false,
    }
  },

  validations: {
    userName: required,
    firstName: required,
    lastName: required,
    email: {
      required,
      email,
    },
    password: { required, minLength: minLength(6) },
  },

  methods: {
    async registerUser() {
      // stop here if form is invalid
      this.$v.$touch()
      if (this.$v.$invalid) {
        return
      }

      // const headers = {
      //   Authorization: `Bearer ${this.$store.state.auth.authData.token}`,
      //   'My-Custom-Header': 'foobar',
      // }

      const response = await axios
        .post('/api/v1/accounts', {
          username: this.userName,
          first_name: this.firstName,
          last_name: this.lastName,
          email: this.email,
          password: this.password,
          is_active: this.isActive,
          is_staff: this.isStaff,
        })
        .catch((error) => console.log(error))

      console.log('status code', response.config.data)
    },
  },
}
</script>

<style scoped>
.invalid-feedback {
  color: red;
}
</style>
