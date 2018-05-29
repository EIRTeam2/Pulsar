<template>
  <div v-show="is_active">
    <slot>
    </slot>
  </div>
</template>

<script>
module.exports = {
  name:"Tab",
  data: function() {
    return {
      is_active: false
    }
  },
  props: {
    name: {
      required: true,
    },
    selected: {
      default: false
    }
  },
  mounted: function() {
    this.is_active = this.selected;
  },
  methods: {
    select_tab: function(selected_tab) {
      event.stopPropagation();
      this.deployed = !this.deployed;
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
