import Vue from "vue";
Vue.component('editable-input', {
data: function () {
  return {
    editing_input: false,
    input_value: ""
  }
},
props: ["property", "editing_object", "resource_type"],
delimiters: ["[[","]]"],
template: '<div class="editable-field"> <p> <strong>[[property.display_name]]</strong> <span class="icon editable-icon" @click="enableEditing"> <i class="fa fa-pencil "> </i> </span> </p><div v-if="!editing_input" class="content"> [[getFieldValueFromEditingObject(property.field)]] </div><input v-if="editing_input" ref="user_input" v-model="input_value" class="input" type="text" placeholder="Text input" v-on:keyup.enter="saveEdit" v-on:keyup.esc="disableEditing"> <p v-if="editing_input" class="has-text-right is-size-7"> Enter to save | ESC to cancel </p></div>',
methods: {
  enableEditing: function(){
    this.editing_input = true;
    this.input_value = this.editing_object[this.property.field];
  },
  getFieldValueFromEditingObject: function(field_name) {
    return this.editing_object[field_name]
  },
  disableEditing: function(){
    this.editing_input = false;
    this.property.value = this.property.pre_edit_value
  },
  saveEdit: function(){
    // However we want to save it to the database
    var client = new $.RestClient('/api/', {"ajax": ajaxOption});
    console.log(this.resource_type)
    client.add('resource', {stringifyData: true, url:this.resource_type})
    var update = {}
    this.editing_object[this.property.field] = this.input_value
    update = this.editing_object
    client.resource.update(this.editing_object.id, update)
    this.editing_input = false;
  }
}
});
