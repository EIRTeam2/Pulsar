<template>
  <div>
    <div class="tabs">
      <ul>
        <li v-for="tab in tabs" v-bind:class="{'is-active': tab.is_active}">
          <a @click="select_tab(tab)">
            {{ tab.name }}
          </a>
         </li>
      </ul>
    </div>
    <div class="tab-details">
      <slot></slot>
    </div>
  </div>
</template>

<script>
module.exports = {
  name:"Tabs",
  data: function() {
    return {
      tabs: []
    }
  },
  created: function() {
    this.tabs = this.$children;
  },
  methods: {
    select_tab: function(selected_tab) {
      this.tabs.forEach(
       function(tab){
         tab.is_active = (selected_tab.name == tab.name)
       })
    }
  }
}
</script>

<style>
</style>
