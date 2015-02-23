(function () {
	'use strict';

	var website = openerp.website;

	website.snippet.animationRegistry.contact_eval_click = website.snippet.Animation.extend({
		selector: ".js_contact_eval",
		
		on_click : function () {
			var self = this;
			
			//reads out form
			var $email = this.$target.find(".js_lead_email");
			var $name = this.$target.find(".js_lead_name");
			var group_id = this.$target.attr("data-id");
			console.log($name.val());
			console.log(group_id);

			
			
			//validates email address
			if ($name.val() == "" || !$email.val().match(/.+@.+/)) {
				this.$target.addClass('has-error');
				return false;
			}
			this.$target.removeClass('has-error');

			//creates lead
			openerp.jsonRpc('/contact_eval/confirm', 'call', {
				'lead_email': $email.length ? $email.val() : false,
				'lead_name': $name.length ? $name.val(): false,
				'group_id': group_id.length ? group_id : false,
			}).then(function (success) {
                self.display_message(success);
            });

		},
		//displays message if request was successful
		display_message: function(success) {
			if (success) {
				this.$target.find(".js_contact_eval_form").addClass("hidden");
				this.$target.find(".js_mg_details").removeClass("hidden");
			}
		},

		start : function () {
			//binds button to function
			var self = this;
			this.$target.find(".js_contact_eval_btn").on("click", _.bind(this.on_click, this));
			this._super();
		},
		
	});

	
})();