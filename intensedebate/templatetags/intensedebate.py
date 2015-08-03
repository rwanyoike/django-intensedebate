from django import template
from django.conf import settings
from django.template import TemplateSyntaxError

register = template.Library()


@register.inclusion_tag("intensedebate/load_wrapper_js.html")
def intensedebate_load(
    intensedebate_acct=None,
    post_id=None,
    post_id_prefix="",
    post_id_suffix="",
    post_url=None,
    post_title=None,
    container_id=None):

    if intensedebate_acct is None:
        intensedebate_acct = getattr(settings, "INTENSEDEBATE_ACCT", None)
        if intensedebate_acct is None:
            raise TemplateSyntaxError("The `intensedebate_load` template " +
                "tag requires a site account number. Either pass it as " +
                "`intensedebate_acct`, or set `INTENSEDEBATE_ACCT` in your " +
                "settings.")

    context = {"idcomments_acct": intensedebate_acct}
    if post_id:
        context["idcomments_post_id"] = "{}{}{}".format(
            post_id_prefix, post_id, post_id_suffix)
    if post_url:
        context["idcomments_post_url"] = post_url
    if post_title:
        context["idcomments_post_title"] = post_title
    if container_id:
        context["idcomments_div"] = container_id
    return context


@register.inclusion_tag("intensedebate/link_wrapper_js.html")
def intensedebate_link():
    return
