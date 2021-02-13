export const getRequestData = (data) => {
    const formData = new FormData()
    Object.defineProperties(data).forEach(([key, value]) => {
        if (key === 'image' && (!value || typeof value === 'string')) {
            return
        }
        formData.append(`${key}`, value)
    })
    return formData
}
