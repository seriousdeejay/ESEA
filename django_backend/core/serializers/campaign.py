from rest_framework import serializers

from ..models import Campaign, EseaAccount, Method, Network
from .esea_account import EseaAccountSerializer

class CampaignSerializer(serializers.ModelSerializer):
    organisation_accounts = EseaAccountSerializer(many=True, read_only=True)
    network = serializers.PrimaryKeyRelatedField(queryset=Network.objects.all())
    method = serializers.SlugRelatedField(queryset=Method.objects.all(), slug_field='name')

    # method = serializers.StringRelatedField()
    class Meta:
        model = Campaign
        fields = ['id', 'name', 'network', 'method', 'organisation_accounts', 'open_survey_date', 'close_survey_date']
        depth = 1

    
    def create(self, validated_data):    
        campaign = Campaign.objects.create(**validated_data)
        for organisation in campaign.network.organisations.all():
            EseaAccount.objects.create(organisation=organisation, method=campaign.method, campaign=campaign)
        return campaign
    
    def update(self, instance, validated_data):
        print('check')
        return instance

    # def to_representation(self, instance):
    #     data = super(CampaignSerializer, self).to_representation(instance)
    #     data['method'] = serializers.StringRelatedField()
    #     return data