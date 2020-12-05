<template>
<div>
    <q-btn v-if="!isMobile" outline size="md" rounded color="white" class="text-weight-bold q-mr-lg" unelevated @click="openDialog(headerCallBack)">
        Обратный звонок
        <q-icon size="1.7em" name="phone_callback" class="q-ml-sm" />
    </q-btn>
    <q-btn v-else size="md" rounded color="secondary" class="text-weight-bold q-mr-lg full-width" unelevated @click="openDialog(headerCallBack)">
        Обратный звонок
        <q-icon size="1.7em" name="phone_callback" class="q-ml-sm" />
    </q-btn>

    <q-btn v-if="!isMobile" rounded color="secondary" class="shadow-0 text-weight-bold q-mr-lg" unelevated @click="openDialog(headerConsult)">
        Консултация
        <q-icon size="1.7em" name="support_agent" class="q-ml-sm" />
    </q-btn>
    <q-btn v-else rounded color="primary" class="shadow-0 text-weight-bold q-mt-md full-width" unelevated @click="openDialog(headerConsult)">
        Консултация
        <q-icon size="1.7em" name="support_agent" class="q-ml-sm" />
    </q-btn>

    <!--    Форма обратной связи  -->

    <q-dialog v-model="dialog">
        <q-card style="min-width: 350px">
            <q-card-section>
                <div class="text-h6 text-secondary">{{ dialogHeader }}</div>
                <p class="q-mt-md">
                    Оставьте ваши контактные данные<br />Мы свяжемся с Вами в ближайшее
                    время
                </p>
            </q-card-section>

            <q-card-section class="q-pt-none">
                <q-input color="secondary" v-model="callBackName" label="Ваше имя">
                    <template v-slot:prepend>
                        <q-icon name="face" />
                    </template>
                </q-input>

                <q-input type="number" color="secondary" v-model="callBackPhone" label="Номер телефона">
                    <template v-slot:prepend>
                        <q-icon name="sim_card" />
                    </template>
                </q-input>
            </q-card-section>

            <q-card-actions align="right" class="text-primary">
                <q-btn flat rounded label="Отмена" v-close-popup />
                <q-btn rounded color="primary" label="Отправить" v-close-popup class="q-pl-md" icon-right="send" unelevated />
            </q-card-actions>
        </q-card>
    </q-dialog>
</div>
</template>

<script>
export default {
    name: "qCallBack",
    data() {
        return {
            isMobile: this.$q.platform.is.mobile,
            dialog: false,
            dialogHeader: "",
            headerCallBack: "Обратный звонок",
            headerConsult: "Консультация",
            callBackName: "",
            callBackPhone: "",
        };
    },
    mounted() {},
    methods: {
        openDialog(header) {
            this.dialog = true;
            this.dialogHeader = header;
        }
    }
};
</script>

<style scoped></style>
