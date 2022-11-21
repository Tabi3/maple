import type { PageServerLoad } from '../$types';

const checkEmpty = (obj: Object) => {
    return obj && Object.keys(obj).length === 0
            && Object.getPrototypeOf(obj) === Object.prototype
}

const toCookieString = (obj: {[key: string]: any}) => {
    let Cookie: string = "";
    Object.entries(obj).forEach((key) => {
        Cookie = Cookie.concat(`${key[0]}=${encodeURI(key[1]).replace("=", "%3D")};`)
    })
    return Cookie
}

export const load: PageServerLoad = async ({ locals }) => {
    if (checkEmpty(locals)) {
        locals.darkmode = false
    }
    return { cookies: toCookieString(locals) }
}