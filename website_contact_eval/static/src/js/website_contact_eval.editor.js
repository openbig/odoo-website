(function () {
    'use strict';

    var website = openerp.website;
    var _t = openerp._t;

    website.snippet.options.contact_eval_snippet = website.snippet.Option.extend({
        on_prompt: function () {
            var self = this;
            return website.prompt({
                id: "contact_eval_group",
                window_title: _t("Add to group"),
                select: _t("Group List"),
                init: function (field) {
                    return website.session.model('crm.case.categ')
                            .call('name_search', ['', []]);
                },
            }).then(function (categ_id) {
                self.$target.attr("data-id", categ_id);
            });
        },
        drop_and_build_snippet: function() {
            var self = this;
            this._super();
            this.on_prompt().fail(function () {
                self.editor.on_remove();
            });
        },
        start : function () {
            var self = this;
            this.$el.find(".js_contact_eval_group").on("click", _.bind(this.on_prompt, this));
            this._super();
        },
        
    });
    website.snippet.options.contact_eval_snippet_ex = website.snippet.Option.extend({
        on_prompt: function () {
            var self = this;
            return website.prompt({
                id: "contact_eval_group_ex",
                window_title: _t("Add to group"),
                select: _t("Group List"),
                init: function (field) {
                    return website.session.model('crm.case.categ')
                            .call('name_search', ['', []]);
                },
            }).then(function (categ_id) {
                self.$target.attr("data-id", categ_id);
            });
        },
        drop_and_build_snippet: function() {
            var self = this;
            this._super();
            this.on_prompt().fail(function () {
                self.editor.on_remove();
            });
        },
        start : function () {
            var self = this;
            this.$el.find(".js_contact_eval_group_ex").on("click", _.bind(this.on_prompt, this));
            this._super();
        },
        
    });
})();
