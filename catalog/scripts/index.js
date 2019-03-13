$((function(context) {
    // utc_epoch comes from index.py
    // console.log('Current epoch in UTC is ' + context.utc_epoch);
    return function(){

        var containers = $('.product-container');
        containers.each(function(i, container){
            // console.log($(c).attr('data-product-id'));
            var pid = $(container).attr('data-product-id');
            // console.log(pid);
            $.ajax({
                url: "/catalog/product.tile/" + pid,
            }).done(function(content){
                // console.log(content);
                $(container).html(content);
            });
        });
    }
})(DMP_CONTEXT.get()));