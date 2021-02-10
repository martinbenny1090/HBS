function toggleMenu() {
    let navigation = document.querySelector('.navigation');
    let toggle = document.querySelector('.toggle');
    navigation.classList.toggle('active');
    toggle.classList.toggle('active');

}

$(document).ready(function () {
    $(".b_mngmnt").hide();
    $(".r_mngmnt").hide();
    $(".h_list").hide();
    $(".payout").hide();
    $(".payment").hide();

    $(".bm").click(function () {
        $(".b_mngmnt").show();
        $(".r_mngmnt").hide();
        $(".h_list").hide();
        $(".payout").hide();
        $(".payment").hide();
    });

    $(".rm").click(function () {
        $(".r_mngmnt").show();
        $(".b_mngmnt").hide();
        $(".h_list").hide();
        $(".payout").hide();
        $(".payment").hide();

    });
    $(".hl").click(function () {
        $(".r_mngmnt").hide();
        $(".b_mngmnt").hide();
        $(".h_list").show();
        $(".payout").hide();
        $(".payment").hide();

    });
    $(".po").click(function () {
        $(".r_mngmnt").hide();
        $(".b_mngmnt").hide();
        $(".h_list").hide();
        $(".payout").show();
        $(".payment").hide();

    });
    $(".pm").click(function () {
        $(".r_mngmnt").hide();
        $(".b_mngmnt").hide();
        $(".h_list").hide();
        $(".payout").hide();
        $(".payment").show();

    });
});


