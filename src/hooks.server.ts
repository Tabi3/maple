import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	event.locals.darkmode = event.cookies.get('darkmode') || "false"
	return resolve(event);
};
