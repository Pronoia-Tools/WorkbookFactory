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
        <div class="rounded-md">
          <!-- user name -->
          <div class="mb-6">
            <label for="user_name" class="sr-only">User Name</label>
            <input
              id="user_name"
              v-model="user_name"
              name="user_name"
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
              :class="{ 'is-invalid': $v.user_name.$error }"
            />
            <div v-if="$v.user_name.$error" class="invalid-feedback">
              <span v-if="!$v.user_name.required">User name is required</span>
            </div>
            <div v-if="isError.username" class="invalid-feedback">
              <span v-for="(error, index) in isError.username" :key="index">
                {{ error }}
              </span>
            </div>
          </div>
          <!-- first name -->
          <div class="mb-6">
            <label for="first_name" class="sr-only">First Name</label>
            <input
              id="first_name"
              v-model="first_name"
              name="first_name"
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
              :class="{ 'is-invalid': $v.first_name.$error }"
            />
            <div v-if="$v.first_name.$error" class="invalid-feedback">
              <span v-if="!$v.first_name.required">First name is required</span>
            </div>
          </div>
          <!-- last name -->
          <div class="mb-6">
            <label for="last_name" class="sr-only">Last name</label>
            <input
              id="last_name"
              v-model="last_name"
              name="last_name"
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
              :class="{ 'is-invalid': $v.last_name.$error }"
            />
            <div v-if="$v.last_name.$error" class="invalid-feedback">
              <span v-if="!$v.last_name.required">Last name is required</span>
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
            <div v-if="isError.email" class="invalid-feedback">
              <span v-for="(error, index) in isError.email" :key="index">
                {{ error }}
              </span>
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
              autocomplete="off"
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
              <span v-if="!$v.password.minLength">
                Password must be at least 8 characters
              </span>
            </div>
            <div v-if="isError.password1" class="invalid-feedback">
              <p v-for="(error, index) in isError.password1" :key="index">
                {{ error }}
              </p>
            </div>
          </div>
          <!-- confirm password -->
          <div class="mb-6">
            <label for="confirm_password" class="sr-only">Password</label>
            <input
              id="confirm_password"
              v-model="confirm_password"
              name="confirm_password"
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
              placeholder="Confirm password"
              :class="{ 'is-invalid': $v.confirm_password.$error }"
            />
            <div v-if="$v.confirm_password.$error" class="invalid-feedback">
              <span v-if="!$v.confirm_password.required">
                Confirm password is required
              </span>
              <span v-if="!$v.confirm_password.minLength">
                Confirm password must be at least 8 characters
              </span>
            </div>
            <div
              v-if="!$v.confirm_password.sameAsPassword"
              class="invalid-feedback"
            >
              <span>Passwords must be identical</span>
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
import { validationMixin } from 'vuelidate'
import { required, email, minLength, sameAs } from 'vuelidate/lib/validators'

export default {
  mixins: [validationMixin],
  layout: 'login',
  data() {
    return {
      user_name: '',
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      confirm_password: '',
      isActive: false,
      isStaff: false,
      isError: {},
    }
  },

  validations: {
    user_name: { required },
    first_name: { required },
    last_name: { required },
    email: {
      required,
      email,
    },
    password: { required, minLength: minLength(8) },
    confirm_password: {
      required,
      minLength: minLength(8),
      sameAsPassword: sameAs('password'),
    },
  },
  created() {
    return this.$v.$touch()
  },
  methods: {
    async registerUser() {
      // stop here if form is invalid
      this.$v.$touch()
      if (this.$v.$invalid) {
        return false
      }

      try {
        const response = await this.$axios.$post(
          '/api/rest-auth/registration/',
          {
            username: this.user_name,
            first_name: this.first_name,
            last_name: this.last_name,
            email: this.email,
            password1: this.password,
            password2: this.confirm_password,
            is_active: this.isActive,
            is_staff: this.isStaff,
          }
        )
        if (response) {
          this.$toast({
            title: 'Success',
            description:
              'Your account registered success. Verification e-mail sent.',
            status: 'success',
            duration: 2000,
            position: 'top-right',
          })
          this.$router.push('/login')
        }
      } catch (error) {
        if (error.response) {
          this.$toast({
            title: 'Failed',
            description: 'Your account registered fail.',
            status: 'error',
            duration: 2000,
            position: 'top-right',
          })
        }
        this.isError = error.response.data
      }
    },
  },
}
</script>

<style scoped>
.invalid-feedback {
  color: red;
  font-size: 12px;
  margin-top: 3px;
}
</style>
