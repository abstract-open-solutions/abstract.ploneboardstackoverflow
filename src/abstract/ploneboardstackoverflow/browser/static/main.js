(function ($) {
    "use strict";


    $(document).ready(function () {
      $('.boardConversation input[name="is_checked"]:not(:disabled)').click(function () {
        var self = this,
            is_checked = $(this).is(':checked'),
            comment_uid = $(this).val();

        // uncheck others
        if (is_checked) {
          $('.boardConversation input[name="is_checked"]').not(self).attr('checked', false);
        }

        // note: there's an error that happens just w/ firefox
        // "no element found" after the call
        // dataType html should solve this but is not
        // and we are setting "204 No content" on server side response
        $.ajax({
          url: './@@checked-update',
          type: 'POST',
          data: {'comment_uid': comment_uid,
                 'is_checked': is_checked},
          dataType: 'html'
        });

      });
    });

}(jQuery));


