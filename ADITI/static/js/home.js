$(document).ready(function () {
    $(".hero__container").hide();
    $(".superBtn").click(function () {
        $(".hero__container").toggle();
    });

    if ($(window).width() < 769 ) {
        // change functionality for smaller screens
        $(".smScreen").show();
        $(".smBtn").show();
        $(".main__section").hide();

        $(".smBtn").click(function () { 
            $(".smFilter").toggle();  
        });

        

    } else {
        // change functionality for larger screens
        $(".smScreen").hide();
        $(".smBtn").hide();
        $(".mainScreen").show();
    } 
    
    
});

