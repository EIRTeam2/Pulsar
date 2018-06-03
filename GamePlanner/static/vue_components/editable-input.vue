<template>
  <div v-bind:class="{'editable-field': !editing_input }" v-click-outside="disableEditing">
      <p> <strong>{{field_display_name}}</strong> <span class="icon editable-icon" @click="enableEditing"> <i class="fa fa-pencil "> </i> </span> </p>
      <div v-if="!editing_input">
        <div v-if="editor == 'markdown'"><vue-markdown :source="editing_object[field_name]">  </vue-markdown></div>
        <div v-if="editor == 'select'"> {{getFieldValueFromEditingObject(field_name).name}} </div>
        <div v-else> {{getFieldValueFromEditingObject(field_name)}} </div>

      </div>

      <div v-if="editing_input">
        <input v-if="editor == 'text'" ref="user_input" v-model="input_value" class="input" type="text" placeholder="Text input" v-on:keyup.enter="saveEdit" v-on:keyup.esc="disableEditing">
        <markdown-editor v-if="editor== 'markdown'" :value="input_value"></markdown-editor>
        <div v-if="editor == 'select'" class="select">
          <select>
            <option v-for="option in options" v-model="input_value">{{option.name}}</option>
          </select>
        </div>
      </div>
      <p v-if="editing_input && editor=='text'" class="has-text-right is-size-7"> Enter to save | ESC to cancel </p>
      <div class="level" v-if="editing_input && (editor=='markdown' || editor=='select')">
        <div class="level-left">

        </div>
        <div class="level-right">
          <a class="button is-success" @click="saveEdit">Save</a>
          <a class="button is-danger" @click="disableEditing">Cancel</a>
        </div>
      </div>
  </div>
</template>

<script>
import {getCookie} from 'scripts/csrf.js';
import VueMarkdown from 'vue-markdown';
import markdownEditor from 'vue_components/markdown_editor.vue';
import vClickOutside from 'v-click-outside'
var rest = require('rest');

var csrf = require('rest/interceptor/csrf')
var mime = require('rest/interceptor/mime')
var client = rest.wrap(csrf, {name: "X-CSRFToken" ,token: getCookie("csrftoken") })
client = client.wrap(mime)

module.exports = {
  name:"EditableInput",
  data: function () {
    return {
      editing_input: false,
      input_value: "",
      selected: {}
    }
  },
  props: ["field_display_name", "field_name", "editing_object", "resource_type", "editor", "options"],
  components: {
    "vue-markdown": VueMarkdown,
    "markdown-editor": markdownEditor
  },
  // Editor can either be text or markdown
  methods: {
    enableEditing: function(){
      this.editing_input = true;
      this.input_value = this.editing_object[this.field_name];
    },
    getFieldValueFromEditingObject: function(field_name) {
      return this.editing_object[field_name]
    },
    disableEditing: function(){
      this.editing_input = false;
    },
    saveEdit: function(){
      // However we want to save it to the database
      var updated_resource = {
        id: this.editing_object.id
      }
      updated_resource[this.field_name] = this.input_value

      client({
        path: "/api/" + this.resource_type + "/" + this.editing_object.id + "/",
        method: "PATCH",
        headers: {
          'Content-Type': 'application/json'
        },
        entity: updated_resource
      }).then(function(response) {
          console.log('response: ', response);
      });

      this.editing_object[this.field_name] = this.input_value
      this.editing_input = false;
    }
  },
  directives: {
    clickOutside: vClickOutside.directive
  }
}
</script>

<style>
.editable-field:hover {
  background-color: #966787;
  color: #fff;

}

.editable-field:hover strong {
  color: #fff;

}

.editable-icon:hover {
  cursor: pointer;
}
.editable-icon {
  visibility: hidden;
}
.editable-field {
  padding: 2px;
}
.editable-field:hover .editable-icon {
  visibility: visible;
}
</style>
