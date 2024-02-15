from django.contrib import admin

from services.models import Service, Plan, Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'plan', 'price')
    model = Subscription

    def price(self, obj):
        return obj.service.full_price - (obj.service.full_price * obj.plan.discount_percent / 100.00)


class PlanAdmin(admin.ModelAdmin):
    list_display = ('plan_type', 'discount_percent')
    model = Plan


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'full_price')
    model = Service


admin.site.register(Service, ServiceAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
