$(document).ready(function() {
    // category
    $(".show-category").click(function(event){
        var url = $(this).attr("data-url");
        $.ajax({
            type: "GET",
            url: url,
            success: function(msg) {
                $("#modal-body").html(msg);
            }
        });
    });
    // product
    $(".show-product").click(function(event){
        var url = $(this).attr("data-url");
        $.ajax({
            type: "GET",
            url: url,
            success: function(msg) {
                $("#modal-body").html(msg);
            }
        });
    });
    // customer
    $(".show-customer").click(function(event){
        var url = $(this).attr("data-url");
        $.ajax({
            type: "GET",
            url: url,
            success: function(msg) {
                $("#modal-body").html(msg);
            }
        });
    });
    // order
    $(".show-order").click(function(event){
        var url = $(this).attr("data-url");
        $.ajax({
            type: "GET",
            url: url,
            success: function(msg) {
                $("#modal-body").html(msg);
            }
        });
    });
});
