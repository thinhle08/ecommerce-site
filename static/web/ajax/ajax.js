$(document).ready(function() {

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
