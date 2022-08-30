$(document).ready(function () {
    $('.minus').click(function () {
        var $input = $(this).parent().find('.cart-qty');
        var count = parseInt($input.val()) - 1;
        var cart_id = $(this).data('cartid')
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        var book_upload_url = $('#cart-update-url').val();
        url = book_upload_url
        $.ajax({
            type: "POST",
            url: url,
            data: {
                'cart_id': cart_id,
                'count': count
            },
            success: function (data) {
                $('#amount').text(data.amount);
                $('#totalamount').text(data.totalamount);
                console.log(data)
            }
        });
        return false;
    });
    $('.plus').click(function () {
        var $input = $(this).parent().find('.cart-qty');
        var cart_id = $(this).data('cartid')
        let count = parseInt($input.val()) + 1
        $input.val(count);
        count = $input.val()    
        var book_upload_url = $('#cart-update-url').val();
        url = book_upload_url
        $.ajax({
            type: "POST",
            url: url,   

            data: {
                'cart_id': cart_id,
                'count': count
            },
            success: function (data) {
               
                $('#amount').text(data.amount);
                $('#totalamount').text(data.totalamount);
            }
        });
        return false;
    });
    
});
$('.remove_cart').click(function (event) {
    remove_this = $(this);
    var cart_id = $(this).attr('data-key')
    console.log(cart_id,'----------cart_id')
    $.ajax({
        type: "POST",
        url: "/remove-cart/",   

        data: {
            'cart_id': cart_id,
            
        },
        success: function (data) {
           if (data.status == 'success'){
            $(remove_this).parent().parent().parent().parent().parent().parent().parent().remove();
            console.log('delete successfully')
           


        }
       
        }
    });
    return false;
    
});