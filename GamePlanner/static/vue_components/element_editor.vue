<template>
  <div>
    <div class="level">
        <div class="level-item">
          <EditableInput :editor="'text'" :resource_type="resource_type"  :field_name="'name'" :field_display_name="'Name'"
                           v-bind:editing_object="editing_object" :key="'name'"  >
          </EditableInput>
        </div>
    </div>

    <div class="content" id="display-description">
      <EditableInput :resource_type="resource_type"  :field_name="'description'" :field_display_name="'Description'"
                       v-bind:editing_object="editing_object" v-bind:editor="'markdown'" :key="'description'"  >
      </EditableInput>
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
  name:"ElementEditor",
  data: function () {
    return {
      is_editing_element: false
    }
  },
  props: {
    properties: {
      required: true
    },
    element: {
      required: true
    },
    element_type: {
      required: true
    },
    has_description: {
      default: false
    }
  },
  components: {
    "vue-markdown": VueMarkdown,
    "markdown-editor": markdownEditor
  },
  // Editor can either be text or markdown
  methods: {

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
