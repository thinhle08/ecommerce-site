$(function(){var e=$(".form-validate-summernote"),t=$(".summernote"),i=e.validate({errorElement:"div",errorClass:"is-invalid",validClass:"is-valid",ignore:":hidden:not(.summernote),.note-editable.card-block",errorPlacement:function(e,n){e.addClass("invalid-feedback"),console.log(n),"checkbox"===n.prop("type")?e.insertAfter(n.siblings("label")):n.hasClass("summernote")?e.insertAfter(n.siblings(".note-editor")):e.insertAfter(n)}});t.summernote({height:300,callbacks:{onChange:function(e,n){t.val(t.summernote("isEmpty")?"":e),i.element(t)}}})});