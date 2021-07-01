<template>
  <div class="container">
    <div class="header fixed w-full bg-white border-b border-gray-400">
      <ul class="flex flex-row items-center">
        <li>
          <img
            src="../static/Sammy.svg"
            alt="logo-icon"
            srcset="../static/Sammy.svg"
            class="w-10 h-10"
          />
        </li>
        <li>
          <router-link to="/" class="nav-link">Home</router-link>
        </li>
        <li>Editor</li>
        <li>
          <router-link to="/login" class="nav-link">Login</router-link>
        </li>
      </ul>
      <router-view></router-view>
    </div>
  </div>
</template>
