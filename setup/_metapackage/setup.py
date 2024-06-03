import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-shopinvader-odoo-shopinvader",
    description="Meta package for shopinvader-odoo-shopinvader Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-sale_cart>=16.0dev,<16.1dev',
        'odoo-addon-sale_cart_step>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_address>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_anonymous_partner>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_api_address>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_api_cart>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_api_cart_step>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_api_sale>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_api_sale_loyalty>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_api_security_sale>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_api_signin_jwt>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_api_wishlist>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_base_url>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_delivery_state>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_es_product_categ>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_fastapi_auth_jwt>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_filtered_model>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_multi_category>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_product>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_product_attribute_set>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_product_brand>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_product_brand_tag>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_product_description>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_product_sale_packaging>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_product_seo>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_product_url>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_restapi>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_restapi_auth_jwt>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_restapi_invoice>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_restapi_sale_packaging>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_sale_cart>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_sale_state>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_schema_address>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_schema_sale>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_schema_sale_state>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_assortment>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_image>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_product_brand>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_product_brand_image>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_product_media>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_product_seo>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_product_stock>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_product_stock_state>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_product_template_multi_link>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_update>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_update_image>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_update_product_brand>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_update_product_brand_image>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_update_product_brand_tag>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_update_product_media>=16.0dev,<16.1dev',
        'odoo-addon-shopinvader_search_engine_update_product_template_multi_link>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
