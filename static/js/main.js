'use strict';

$(".custom-select-option").click(function() {
    console.log($("#" + $(this).data("target") + "_filter"));
    $("#" + $(this).data("target") + "_filter").innerHTML = $(this).val();
})