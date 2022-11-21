<script lang="ts">
	import '../app.css';
	import { onMount } from 'svelte';
	export let data: any;
	let docm: Document;
	let body: HTMLElement | null;
	let acc: HTMLElement | null;
	let hls: HTMLElement | null;
	let hbj: HTMLElement | null;
	let hvd: HTMLCollectionOf<HTMLElement | Element>;
	let hvr: Array<string>;

	let cookies = (doc: Document) => {
		return document.cookie.split('; ').reduce((prev: { [key: string]: any }, current) => {
			const [name, ...value]: string | string[] = current.split('=');
			prev[name] = value.join('=');
			return prev;
		}, {});
	};
	let darkmode = () => {
		body?.classList.toggle('dark');
		body?.classList.toggle('bg-[#111]');
		body?.classList.toggle('text-white');
		docm.cookie = 'darkmode=false;';
		if (body?.classList.contains('dark')) docm.cookie = 'darkmode=true;';
	};
	let exphls = () => {
		hls?.classList.toggle('expanded');
		acc?.classList.remove('expanded');
	};
	let expacc = () => {
		acc?.classList.toggle('expanded');
		hls?.classList.remove('expanded');
	};
	onMount(() => {
		docm = document;
		body = document.querySelector('body');
		acc = document.getElementById('acc');
		hls = document.getElementById('hls');
		hbj = document.getElementById('hovered-obj');
		hvd = document.getElementsByClassName('ho');
		hvr = ['Account', 'Toggle Dark Mode', 'Hyperlinks'];
		Array.from(hvd).forEach((a: HTMLElement | Element, b: number) => {
			if (a instanceof HTMLElement) {
				a.onmouseover = () => {
					if (hbj != undefined) {
						hbj.innerHTML = hvr[b];
						hbj.classList.toggle('opacity-0');
					}
				};
				a.onmouseleave = () => {
					if (hbj != undefined) {
						hbj.classList.toggle('opacity-0');
					}
				};
			}
		});
		document.cookie = data.cookies;
		if (cookies(docm).darkmode === 'true') {
			darkmode();
		}
		console.log(cookies(docm));
	});
</script>

<svelte:body class="duration-100" />
<div
	class="shadow-md fixed bg-inherit z-50 
		   pastel-line-x w-screen"
>
	<div class="top-0 left-0 mx-auto w-[1280px] flex flex-row gap-2 py-2">
		<button class="bx bxs-user p-3 widget ho" on:click={expacc} />
		<button class="bx bxs-moon p-3 widget ho" on:click={darkmode} />
		<button class="bx bxs-grid-alt p-3 widget ho" on:click={exphls} />
		<p id="hovered-obj" class="duration-200 opacity-0 p-2 text-slate-500" />

		<form action="" class="inline-flex ml-auto gap-2">
			<input type="text" class="px-4 p-1 widget" placeholder="search" />
			<button class="bx bxs-search p-3 widget" />
		</form>
	</div>
</div>
<div class="w-screen top-16 fixed h-0 z-50 overflow-visible">
	<div class="w-[1280px] mx-auto h-0 overflow-visible">
		<div class="closed flex-wrap" id="hls">
			<a href="/" class="gr-ul aspect-square"><i class="bx bxs-home-alt-2" /></a>
			<a href="/school" class="gr-ul aspect-square"><i class="bx bxs-graduation" /></a>
			<a href="/calculator" class="gr-ul aspect-square"><i class="bx bx-math" /></a>
			<a href="/maple-bot" class="gr-ul aspect-square"><i class="bx bxs-leaf" /></a>
		</div>
		<div class="closed flex-col" id="acc">
			<a href="/" class="gr-ul"><i class="bx bxs-home-alt-2" /> Home</a>
			<a href="/" class="gr-ul"><i class="bx bxs-graduation" /> Khub</a>
			<a href="/" class="gr-ul"><i class="bx bx-math" /> Wolfram Alpha</a>
		</div>
	</div>
</div>

<slot />
<div class="bg-[#efefef] shadow-md py-16 mt-16 flex items-center">
	<div class="m-auto card flex-row grid w-[1280px]" style="grid-template-columns: 1fr 2fr;">
		<div class="!bg-inherit">
			This is the footer. If you're at the school tab then you may see it bugged. this is because
			the body element is still too short
		</div>
		<div class="!bg-inherit">
			This part of the footer will contain hyperlinks to companies / sponsors. This can also display
			the site description, vision or mission.
		</div>
	</div>
</div>
