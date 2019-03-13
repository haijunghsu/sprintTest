$((function(context){
    return function(){
        $.ajax({
            //write a getTile function inside index.py
            "url": "/catalog/index.gettile/"
        }).done(function(data){
            $('#cooltiltle').html(data);
        });
    }
})(DMP_CONTEXT.get()));