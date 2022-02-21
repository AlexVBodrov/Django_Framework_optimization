$('.formset_row').formset({
    addText: 'добавить продукт',
    addCssClass: 'btn btn-outline-primary btn-block',
    deleteText: 'удалить',
    deleteCssClass: 'btn btn-outline-warning',
    prefix: 'orderitems',
    added: setDefaultValue,
    removed: itemDelete,
    hideLastAddForm: false,
});