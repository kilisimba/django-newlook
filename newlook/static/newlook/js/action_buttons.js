$(function() {
    $(".actions label").hide();
    $(".actions button").hide();
    
    // Arrange the select options to list
    var mappedItems = $( ".actions option").map(function() {
        if ( $(this).val() ) {
            var itemlist = $("<li>").append($("<a href>").text($(this).text()));
            itemlist.children().attr("id", $(this).val());
            return itemlist.get(0);
        }
    })
    // $(".actions").prepend( $("<ul id='action-buttons'>").append(mappedItems) );
    $("ul.object-tools").prepend( mappedItems );

    // Move the add button to the end of list
    // var addButton = $("ul.object-tools").children().filter("li");
    // $(".actions ul#action-buttons").append(addButton);
    
    // $(".actions #action-buttons a").click(function(ev) {
    $(".object-tools li a").click(function(ev) {
        if ( this.id ) {
            $(".actions option[selected]").removeAttr("selected");
            $(".actions option").filter("[value='" + this.id + "']").attr("selected", "selected");
            $(".actions :button").click();
            // Prevent default event from occuring
            return false;
        }
        return true;
    })
});
