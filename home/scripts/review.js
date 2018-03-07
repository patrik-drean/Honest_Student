$(function(context) {
   return function() {
      var stars_wrap = $('.star_wrap')

      stars_wrap.hover(
        function() {
           var starNumber = ($(this).attr('class').split(/\s+/))[1];

          hoverStars(starNumber)
        }, function() {
          unHoverStars();
        }
      );

      stars_wrap.click(function() {
         var starNumber = ($(this).attr('class').split(/\s+/))[1];
         clickStars(starNumber);

         stars_wrap.off('mouseenter mouseleave');
      });



}

}(DMP_CONTEXT.get()))

// The color fill for the svg tags

var colorFilled = 'M259.3 17.8L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0z'

var colorOutlined = 'M528.1 171.5L382 150.2 316.7 17.8c-11.7-23.6-45.6-23.9-57.4 0L194 150.2 47.9 171.5c-26.2 3.8-36.7 36.1-17.7 54.6l105.7 103-25 145.5c-4.5 26.3 23.2 46 46.4 33.7L288 439.6l130.7 68.7c23.2 12.2 50.9-7.4 46.4-33.7l-25-145.5 105.7-103c19-18.5 8.5-50.8-17.7-54.6zM388.6 312.3l23.7 138.4L288 385.4l-124.3 65.3 23.7-138.4-100.6-98 139-20.2 62.2-126 62.2 126 139 20.2-100.6 98z'

// Functions to hover, unhover, and click

function hoverStars(starNumber) {
   var stars = $('path')
   stars.each(function( index, element ) {

   stars_wrap = $(this).parent().parent()
    $( element ).attr('d', colorFilled);
    if ( stars_wrap.hasClass(starNumber)) {
      return false;
    }
  });


}
function unHoverStars() {
   var stars = $('path')
   stars.attr('d', colorOutlined);
}

function clickStars(starNumber) {
   var stars = $('path')
   var booleanStar = true
   // Go through each star to give its color until it hits the indicated star
   stars.each(function( index, element ) {

   if (booleanStar)
   {
       $( element ).attr('d', colorFilled);

       stars_wrap = $(this).parent().parent();
       if ( stars_wrap.hasClass(starNumber))
       {
         booleanStar = false;
       }
   }
   else
   {
       $( element ).attr('d', colorOutlined);
   }
});
}
