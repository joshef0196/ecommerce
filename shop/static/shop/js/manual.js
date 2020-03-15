


$("#create_account").change(function() { 
    if($('#create_account').is(':checked')) {
        $("#password, #password_lbl").prop("hidden", false);
        $("#password").prop("required", true);
    }
    else {
        $("#password, #password_lbl").prop("hidden", true);
        $("#password").prop("required", false);
    }
});


$("#checkout").click(function() {
    var confirm_msg = confirm("Do you want to place order?");
    if(confirm_msg){
        $.ajax({
            url: '/checkout/',
            data: {
                'cus_name': $('#cus_name').val(),
                'cus_email': $('#cus_email').val(),
                'cus_add1': $('#cus_add1').val(),
                'cus_phone': $('#cus_phone').val(),
                'cus_postcode': $('#cus_postcode').val(),
                'cus_state': $('#cus_state').val(),
                'cus_city': $('#cus_city').val(),
                'password': $('#password').val(),
                'create_account': $('#create_account').val(),
            },
            success: function (data) {
                if(data["status"] == "success"){
                    $("#email_id").val(data["cus_email"]);
                    $("#tracsaction_id").val(data["invoice_no"]);
                    $("#checkoutForm").submit();
                }
                else {
                    alert('Someting went wrong!');
                    window.location("/");
                }
            }
        });
    }
});