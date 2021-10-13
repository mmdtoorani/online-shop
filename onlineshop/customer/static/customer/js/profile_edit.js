$("#button").on("click", function () {
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/api/customers/edit_profile/",
        data: $('#form').serialize(),

        success: function (data) {
            console.log('Im in success!');
            console.log(data);
        },
        error: function () {
            console.log('ERROR!!!');
            console.log(this.data);
        }
    })
})