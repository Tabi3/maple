<script lang="ts">
	import { onMount } from 'svelte';
</script>

<div class="banner">
	<div class="!bg-transparent w-screen flex gap-8 flex-col">
		<div style="background-color: rgba(0, 0, 0, 0.5);" class="w-screen p-8">
			<div class="w-[1280px] m-auto !bg-transparent flex gap-4">
				<div class="!bg-transparent flex flex-col gap-8">
					<h1 class="text-9xl text-white flex items-center gap-8">
						Cloudbound <i class="bx bxs-cloud" />
					</h1>
					<p class="text-3xl text-white">Data Bounded to the Clouds</p>
				</div>
			</div>
		</div>
		<div class="w-[1280px] m-auto !bg-transparent flex gap-4 items-center p-4">
			<a href="" class="hov-btn hover:!bg-[rgba(0,0,0,0.5)]">Random Ass Name</a>
			<ul
				class="flex flex-row gap-8 items-center w-1/6 rounded-md 
					text-white justify-center py-4 bg-[rgba(0,0,0,0.5)]"
			>
				<li class=""><i class="bx bxs-home-alt-2" /></li>
				<li class=""><i class="bx bxs-graduation" /></li>
				<li class=""><i class="bx bx-math" /></li>
			</ul>
		</div>
	</div>
</div>
<div class="m-auto w-[1280px] pt-20 py-2">
	<main class="grid grid-cols-2 gap-4 px-4">
		<div class="card col-span-2">
			<h1 class="text-3xl">What is Cloud Bound?</h1>
			<p>
				Remember Maple? Yeah, the website design looked bad after a while. It was due to very poor
				designing coming from my part. However, I have grown, therefore Cloud Bound changes that.
			</p>
			<h1>Cloud Bound also offers new features such as:</h1>
			<ul class="pastel-line-y overflow-hidden rounded-md relative font-mono !bg-[#111] text-white">
				<li class="p-1">Added widgets for school.</li>
				<li class="p-1">Added Cloud storage.</li>
				<li class="p-1">Added Account system.</li>
			</ul>
			<p>Don't forget about Maple Bot too.</p>
			<button class="hov-btn bxl-discord relative isolate">
				<img
					src="https://cdn.discordapp.com/attachments/956813186026315777/1035516677913313280/unknown.png"
					alt="Wolfram"
					class="absolute opacity-0 m-auto
					 w-full h-full top-0 left-0 p-4 blur-sm -z-10"
				/>
				Click here to invite Maple
			</button>
		</div>
		<div class="w-full p-4 flex flex-col gap-8">
			<h1 class="text-2xl">Hello Teacher!</h1>
			<p>
				Just so you know This is temporary text. But since it's just a quarter project then i guess
				this is ok. Its a svelte project so some features might not work for you like the dark mode
				feature since i will preproccess it to static html.
			</p>
			<ul><span class="text-emerald-400">HOWEVER.</span> I will try to fix them.</ul>
			<div class="py-2 pastel-line-y overflow-hidden relative rounded-md bg-[#111] text-white">
				<table class="table-auto border-collapse ml-2 mr-2">
					<thead>
						<tr>
							<td class="border-slate-600 border-b-[1px] font-bold p-2">Question</td>
							<td class="border-slate-600 border-b-[1px] font-bold p-2">Answer</td>
						</tr>
					</thead>
					<tr>
						<td class="border-slate-600 border-b-[1px] p-2">This is a table</td>
						<td class="border-slate-600 border-b-[1px] p-2">It is pretty neat</td>
					</tr>
					<tr>
						<td class="border-slate-600 border-b-[1px] p-2">However they're hard to deal with</td>
						<td class="border-slate-600 border-b-[1px] p-2">This is why Grids are superior</td>
					</tr>
					<tr>
						<td class="border-slate-600 border-b-[1px] p-2">But tables existed before grids</td>
						<td class="border-slate-600 border-b-[1px] p-2"
							>so there are alot of websites that rely on tables</td
						>
					</tr>
				</table>
			</div>
		</div>
		<div class="card">
			<h1 class="text-3xl">Cloudbound Features</h1>
			<p>
				Cloudbound is a cloud computing platform, meaning you can do calculations and store data
				here to use on another device. Not only this, it also has
			</p>
			<ul class="pastel-line-y overflow-hidden rounded-md relative font-mono !bg-[#111] text-white">
				<li class="p-1">Reskinning Websites</li>
				<li class="p-1">Calendar Feature</li>
				<li class="p-1">School tools (exclusive to PSHS CVC scholars)</li>
			</ul>
			<p>The school tools are powered by Wolfram Alpha and Maple Bot (WIP).</p>
			<h1 class="text-xl">Links to websites</h1>
			<div class="flex flex-row ">
				<a href="" class="hov-btn m-1 w-full relative isolate" id="Wolfram">
					<img
						src="https://www.wolframalpha.com/_next/static/images/Logo_1t99UmgS.svg"
						alt="Wolfram"
						class="absolute opacity-0 m-auto
						 w-full h-full top-0 left-0 p-4 blur-sm -z-10"
					/>
					Wolfram Alpha
				</a>
				<a href="" class="hov-btn m-1 w-full relative isolate" id="PSHSCVC">
					<img
						src="https://khub.cvc.pshs.edu.ph/pluginfile.php/1/theme_moove/logo/1666863919/pshs_new_logo.png"
						alt="Wolfram"
						class="absolute opacity-0 m-auto
						 w-full h-full top-0 left-0 p-4 blur-sm -z-10"
					/>
					PSHS Khub
				</a>
				<a href="" class="hov-btn m-1 w-full relative isolate" id="Maplebt">
					<img
						src="https://cdn.discordapp.com/attachments/956813186026315777/1035516677913313280/unknown.png"
						alt="Wolfram"
						class="absolute opacity-0 m-auto
						 w-full h-full top-0 left-0 p-4 blur-sm -z-10"
					/>
					Maple Bot
				</a>
			</div>
		</div>
		<div class="card">
			<h1 class="text-3xl">Why use Cloudbound</h1>
			<p>
				I admit Cloudbound is a weak alternative to competition, mainly google and other massive
				tech companies. So if you picked Cloudbound then Idk what's going on in your mind bro.
			</p>
			<p>Here's a video about clouds... literally...</p>
		</div>
		<iframe
			width="100%"
			class="aspect-video rounded-md"
			src="https://www.youtube.com/embed/EK_UOLsN72Q"
			title="☁️ What is a Cloud? Crash Course Geography #10"
			frameborder="0"
			allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
			allowfullscreen
		/>
		<i class="col-span-2 pastel-line-x relative h-[2px] overflow-hidden rounded-full" />
		<div class="col-span-2 card">
			<h1 class="text-xl">REMINDERS</h1>
			<ul class="pastel-line-y overflow-hidden rounded-md relative font-mono !bg-[#111] text-white">
				<li class="p-1">99% of the features of this website hasn't been developed yet</li>
				<li class="p-1">
					The navbar has the accounts widget, the dark mode toggle, and the hyperlinks
				</li>
				<li class="p-1">
					Only one of the hyperlinks work and that is <i class="bx bxs-graduation" /> which is the school
					part
				</li>
				<li class="p-1">
					The search bar is basically useless. Accounts have not been implemented yet. The school
					hyperlink will be used as a hub for sites.
				</li>
				<li class="p-1">
					Dark Mode also isn't persistent because cookie implementation is too hard.
				</li>
			</ul>
		</div>
	</main>
</div>

<style>
</style>
