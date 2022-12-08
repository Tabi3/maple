<script lang="ts">
	import '../../app.css';
	import { onMount } from 'svelte';
	export let data: any;
	let docm: Document;

	let cookies = (doc: Document) => {
		return document.cookie.split('; ').reduce((prev: { [key: string]: any }, current) => {
			const [name, ...value]: string | string[] = current.split('=');
			prev[name] = value.join('=');
			return prev;
		}, {});
	};
	onMount(() => {
		docm = document;
		document.cookie = data.cookies;
	});
</script>

<svelte:body class="duration-100 {cookies(docm).darkmode === 'true' ? 'dark' : ''}" />
<div class="left-sidebar">
	<h1 class="text-2xl">School tools</h1>
	<ul>
		<li><a href="/" class="gr-ul p-2">Item (Redirects to Home)</a></li>
		<li><a href="/" class="gr-ul p-2">Item (Redirects to Home)</a></li>
		<li><a href="/" class="gr-ul p-2">Item (Redirects to Home)</a></li>
	</ul>
</div>
<div class="right-sidebar">
	<h1 class="text-2xl">Ad Area?</h1>
	<ul>
		<li><a href="/" class="gr-ul p-2">Could be listings</a></li>
		<li><a href="/" class="gr-ul p-2">Could be messages</a></li>
		<li><a href="/" class="gr-ul p-2">Could be the KHUB Courses</a></li>
	</ul>
</div>
<div class="main-container w-[720px]">
	<main class="flex gap-8 flex-col ov">
		<slot />
	</main>
</div>