<template>
      <div class="box task-box">
        <p><span class="icon"><i class="fa fa-sitemap"></i></span> <strong>{{task.design_element.name}} </strong></p>
        <p><strong>#{{task.id}} </strong>{{task.title}}</p>
        <p>{{task.category.name}} | {{task.sub_category.name}}</p>
      </div>
</template>
<script>
module.exports = {
  name:"Task",
  props: {
    task: {}
  },
  data: function() {
    return {
    }
  },
  methods: {

  }
}
</script>

<style>
.scolumns {
    flex-wrap: wrap;
    align-items: stretch;
}

.scolumn {
  min-height: 300px;
}

.task-box {
  border-radius: 0;
  left: 10px;
  margin-bottom: 0;
  box-shadow: none;
  border: none;
  background-color: #FFF;
}

</style>
