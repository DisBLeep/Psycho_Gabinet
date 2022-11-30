function switchTab(e) {
    $('.panel-btn').removeClass('btn-active').addClass('btn-inactive');
    $('#'+ e).removeClass('btn-inactive').addClass('btn-active');
    $('.panel').hide();
    $('#panel-'+ e).show()
}
