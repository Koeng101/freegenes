'''

Copyright (C) 2019 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

'''

from django.conf.urls import (
    url, 
    include
)
import rest_framework.authtoken.views as authviews
from rest_framework import routers
from fg.apps.api.urls.serializers import (
    AuthorViewSet,
    ContainerViewSet,
    CollectionViewSet,
    CompositePartViewSet,
    DistributionViewSet,
    InstitutionViewSet,
    ModuleViewSet,
    OperationViewSet,
    OrderViewSet,
    OrganismViewSet,
    PartViewSet,
    PlanViewSet,
    PlateViewSet,
    PlateSetViewSet,
    ProtocolViewSet,
    RobotViewSet,
    SampleViewSet,
    SchemaViewSet,
    TagViewSet
)



router = routers.DefaultRouter()
router.register(r'^authors', AuthorViewSet, base_name="author")
router.register(r'^containers', ContainerViewSet, base_name="container")
router.register(r'^collections', CollectionViewSet, base_name="collection")
router.register(r'^compositeparts', CompositePartViewSet, base_name="compositepart")
router.register(r'^distributions', DistributionViewSet, base_name="distribution")
router.register(r'^institutions', InstitutionViewSet, base_name="institution")
router.register(r'^modules', ModuleViewSet, base_name="module")
router.register(r'^operations', OperationViewSet, base_name="operation")
router.register(r'^orders', OrderViewSet, base_name="order")
router.register(r'^organisms', OrganismViewSet, base_name="organism")
router.register(r'^parts', PartViewSet, base_name="part")
router.register(r'^plans', PlanViewSet, base_name="plan")
router.register(r'^platesets', PlateSetViewSet, base_name="plateset")
router.register(r'^plates', PlateViewSet, base_name="plate")
router.register(r'^protocols', ProtocolViewSet, base_name="protocol")
router.register(r'^robots', RobotViewSet, base_name="robots")
router.register(r'^schemas', SchemaViewSet, base_name="schemas")
router.register(r'^samples', SampleViewSet, base_name="samples")
router.register(r'^tags', TagViewSet, base_name="tag")

urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', authviews.obtain_auth_token),

]
