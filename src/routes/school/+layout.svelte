<script lang="ts">
    import '../../app.css'
    import { onMount } from 'svelte';
	export let data: any;
	let docm: Document;

	let cookies = (doc: Document) => {
		return document.cookie.split('; ').reduce((prev: {[key : string]: any}, current) => {
			const [name, ...value]: string | string[] = current.split('=');
			prev[name] = value.join('=');
			return prev;
		}, {});
	}
	onMount(() => {
		docm = document
		document.cookie = data.cookies
	});
</script>

<svelte:body class="duration-100 {cookies(docm).darkmode === 'true' ? 'dark': ''}"/>
<div class="shadow-md fixed top-10 flex h-screen w-[18rem] p-10 left-0 z-40 
			dark:!bg-[#121212] flex-col gap-4">
	<h1 class="text-2xl">School tools</h1>
	<ul class="pastel-line-y overflow-hidden relative rounded-md">
		<li><a href="/" class="gr-ul p-2">Item (Redirects to Home)</a></li>
		<li><a href="/" class="gr-ul p-2">Item (Redirects to Home)</a></li>
		<li><a href="/" class="gr-ul p-2">Item (Redirects to Home)</a></li>
	</ul>
</div>
<div class="shadow-md fixed top-10 flex h-screen w-[18rem] p-10 right-0 z-40 
			dark:!bg-[#121212] flex-col gap-4">
	<h1 class="text-2xl">Ad Ar ea?</h1>
	<ul class="pastel-line-y overflow-hidden relative rounded-md">
		<li><a href="/" class="gr-ul p-2">Could be listings</a></li>
		<li><a href="/" class="gr-ul p-2">Could be messages</a></li>
		<li><a href="/" class="gr-ul p-2">Could be the KHUB Courses</a></li>
	</ul>
</div>
<main class="pl-[19rem] pt-[4.5rem] p-4 w-[calc(100%_-_20rem)] flex gap-8">
	<slot />
</main>
