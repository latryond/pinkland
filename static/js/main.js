'use strict';

$(".custom-select-option").click(function() {
    var target = $(this).data("target");
    $(`#${target}_filter`).html($(this).html());
})

$("#query_submit").click(function() {
    var t = $("#type_filter").html();
    var p = $("#part_filter").html();
    var f = $("#function_filter").html();
    window.location = `http://www.pinkland.com.hk/product/${t}/${p}/${f}`;
})