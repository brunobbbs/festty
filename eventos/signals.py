#-*- coding: utf-8 -*-

from django.template.defaultfilters import slugify


def create_slug(sender, instance, signal, *args, **kwargs):

    # Checando os atributos
    if instance.id and hasattr(instance, 'slug_field_name') and hasattr(instance, 'slug_from'):

        # Salvando informação do slug
        slug_name = instance.slug_field_name
        slug_from = instance.slug_from
        
        # Configurando slug se vazio
        if not getattr(instance, slug_name, None):
            # Criando slug
            slug = '%s/%s-' % (instance.id, slugify(getattr(instance, slug_from)))

            # Configurando slug
            setattr(instance, slug_name, slug)

            # Salvando instance
            instance.save()
