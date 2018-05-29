<template>
  <vddl-draggable :selected="callback" class="panel__body--item" :key="node.id" :draggable="node" :index="index" :wrapper="nodes" effect-allowed="move">
      <div v-if="node.children.length > 0" class="item-box box" v-bind:class="{'box-selected': node.id == selected_node.id}">
        <span class="icon deploy-icon" v-on:click="toggle_button($event)">
          <i class="fa" v-bind:class="{'fa-chevron-down': deployed, 'fa-chevron-right': !deployed }"></i>
        </span>
        <span>{{node.name}}</span>
      </div>
      <vddl-list :inserted="on_inserted" :list="node.children" :horizontal="false" v-bind:class="{'item-box box childless-list': node.children.length <= 0, 'children-list': node.children.length > 0, 'box-selected': node.id == selected_node.id && node.children.length <= 0}">
            <div v-if="node.children.length <= 0">
              <span>{{node.name}}</span>
            </div>
            <TreeItem v-if="deployed" v-for="(child, c_index) in node.children" :selected_node="selected_node" :callback="callback" :index="c_index" :nodes="node.children" :key="child.id" :node="child">
            </TreeItem>
            <vddl-placeholder class="red is-size-7">Drop to add as children</vddl-placeholder>
      </vddl-list>
  </vddl-draggable>
</template>

<script>
import {getCookie} from 'scripts/csrf.js';

var rest = require('rest');

var csrf = require('rest/interceptor/csrf')
var mime = require('rest/interceptor/mime')
var client = rest.wrap(csrf, {name: "X-CSRFToken" ,token: getCookie("csrftoken") })
client = client.wrap(mime)
module.exports = {
  name:"TreeItem",
  props: ["node", "nodes", "index", "callback", "selected_node"],
  data: function() {
    return {
      deployed: true,
    }
  },
  methods: {
    toggle_button: function(event) {
      event.stopPropagation();
      this.deployed = !this.deployed;
    },
    on_inserted : function(result) {
      console.log(result.item.name + " is now a child of " + this.node.resource_url)
      console.log(result.item)
      var resulted = result.item
      var resulting_entity = {
          id: result.item.id,
          parent: {pk: this.node.id},
      }
      client({
        path: "/api/design_element/" + result.item.id + "/",
        method: "PATCH",
        headers: {
          'Content-Type': 'application/json'
        },
        entity: resulting_entity
      }).then(function(response) {
          console.log('response: ', response);
      });

    }
  }
}
</script>

<style>
.box:not(:last-child) {
  margin-bottom: 0;
}

</style>
