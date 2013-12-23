from django import template

register = template.Library()


@register.inclusion_tag('intensedebate/config_js.html')
def intensedebate_config(intensedebate_acct=None, post_id=None, post_url=None, post_id_prefix='', post_id_suffix=''):
    from django.conf import settings
    from django.template import TemplateSyntaxError

    if intensedebate_acct is None:
        intensedebate_acct = getattr(settings, 'INTENSEDEBATE_ACCT', None)

    if intensedebate_acct is None:
        raise TemplateSyntaxError(
            'The `intensedebate_config` template tag requires a `intensedebate_acct`. You must either pass it as an argument or set INTENSEDEBATE_ACCT in your settings.')

    if post_id is None:
        raise TemplateSyntaxError(
            'The `intensedebate_config` template tag requires a `post_id`. You must pass it as an argument.')

    return {
        'idcomments_acct': intensedebate_acct,
        'idcomments_post_id': "%s%s%s" % (post_id_prefix, post_id, post_id_suffix),
        'idcomments_post_url': post_url,
    }


@register.inclusion_tag('intensedebate/load_wrapper_js.html')
def intensedebate_cw():
    return


@register.inclusion_tag('intensedebate/link_wrapper_js.html')
def intensedebate_lw():
    return
