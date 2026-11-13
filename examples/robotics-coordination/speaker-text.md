# Multi-Agent Coordination: English speaker text

Aligned to the 46-slide retained demo. Detailed source links are listed per slide. Numerical statements remain historical claims of the original November 2026 snapshot; see README.md.

## Slide 01 - Multi-Agent Coordination

**The focus today is how agents work together, especially when those agents are robots.** I’ll start with the wider research landscape, then use robot teams to show why coordination matters and what it takes for a team to adapt while it’s working.

Source details: see the slide hyperlinks and sources.json.

## Slide 02 - Agenda

The talk starts with the wider landscape, then focuses on robotics, its milestones and current evidence. It ends with experiments to test whether teams can keep working when circumstances change.

Source details: see the slide hyperlinks and sources.json.

## Slide 03 - Two robots must coordinate to lift one basket

**Both robots need a secure grip before they lift.** In this frame from Stanford’s CHORUS experiment, the ARX on the left holds one handle and the Kinova on the right holds the other. Each arm can reach its own handle. The hard part is timing the lift. If the Kinova moves before the other arm has a grip, the basket can slip, which is what the authors observed with a baseline. That’s a timing dependency and a concrete example of Malone and Crowston’s definition of coordination. In CHORUS, each robot times its movement from its own camera view. Across multi-agent systems, dependencies can also involve information or shared resources. The next slide shows how often those coordination problems appear in the literature.

Sources: [Malone & Crowston (1994)](https://crowston.syr.edu/sites/default/files/acmcs94.pdf) · [Jennings (1993)](https://www.cambridge.org/core/journals/knowledge-engineering-review/article/abs/commitments-and-conventions-the-foundation-of-coordination-in-multiagent-systems/0413A9561EBA36994A0C465F6A37436F) · [Stanford · Full-basket demo](https://chorus-model.github.io/static/videos/web/chorus-full-basket.mp4) · [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1)

## Slide 04 - Expanded keyword matches per 1,000 records rose after 2023

**Coordination-related titles became more common in this conference panel after 2023.** The rate rose from 4.76 to 11.60 per thousand records by 2026. That’s about 2.4 times the 2023 rate. The number on the right, 1,445, is the size of the broader candidate pool, while the line shows the yearly frequency of title matches. The trend tells us that these questions are more visible in the panel. Which questions grew most?

Sources: [NeurIPS 2026 program](https://neurips.cc/Downloads/2026) · [ACL Anthology](https://aclanthology.org/) · [ICML Proceedings](https://proceedings.mlr.press/) · [ICLR Proceedings](https://proceedings.iclr.cc/) · [RSS Proceedings](https://roboticsproceedings.org/) · [NeurIPS proceedings](https://proceedings.neurips.cc/)

## Slide 05 - Adaptive coordination leads the 2026 coded subset

**The lead changes across these five years.** Learned self-organization leads in 2022 and 2023. It ties with adaptation in 2024, and adaptation leads in the last two years. In 2026 it accounts for 71 of the 161 coded records, about 44 percent. The next two directions are learned self-organization at 35 and verifiable execution at 29. Adaptation asks whether a team can reassign work or change its plan when conditions change. The next slide compares the same directions across the full period.

Sources: [ACL Anthology](https://aclanthology.org/) · [ICML Proceedings](https://proceedings.mlr.press/) · [ICLR Proceedings](https://proceedings.iclr.cc/) · [RSS Proceedings](https://roboticsproceedings.org/) · [NeurIPS proceedings](https://proceedings.neurips.cc/) · [NeurIPS 2026 program](https://neurips.cc/Downloads/2026)

## Slide 06 - Adaptation and learned coordination lead the coded subset

**Across all five years, adaptation and learned self-organization lead, at 129 and 87 records.** The distinction is useful. Adaptation asks how the team changes course when a plan stops working. Learned self-organization asks how agents learn roles or coordination rules in the first place. Verifiable execution, at 47, asks how to check that a shared action happened as intended. Those are three different technical goals. Next, let’s see the downstream tasks on which researchers evaluate coordination.

Source details: see the slide hyperlinks and sources.json.

## Slide 07 - Robotics ranks third among evaluated application domains

**Robotics ranks third among the downstream applications in this evaluation sample, close to the first two.** Agent economies has 39 studies, software and coding has 37, and robotics and embodiment has 36. The preceding chart was about the research question. This separate sample tells us where methods are tested, from negotiating trades to developing software to executing physical tasks. A study may contribute to several bars. I’ll focus on what changes when those same coordination problems have to be solved by robots in a shared space.

Source details: see the slide hyperlinks and sources.json.

## Slide 08 - Robotics adds physical constraints to coordination

**Coding agents, market agents, and robots share three problems.** They need to allocate work, manage dependencies, and recover when something changes. The constraints are different in each domain. For allocation, coding agents can divide implementation and tests by expertise. A buyer agent has to match its budget and needs to sellers with limited capacity, often with different incentives. A robot assignment depends on reach, payload, and travel time. For dependencies, coding agents need compatible edits and tests that run against the right repository version. Buyers may compete for the last item. Two robots sharing an aisle can block each other, and in the basket lift both grips must be secure before either side lifts. Finally, recovery can mean fixing or reverting a patch in coding, or searching for another offer in a market. A robot that loses its grip may first have to stabilize the load. That’s the distinctive requirement here. The physical state has to stay safe while the team changes its plan. Which research directions are already addressing those constraints?

Sources: [OpenHands](https://arxiv.org/abs/2407.16741) · [Magentic Marketplace](https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/multi-agent-marketplace.pdf) · [CHORUS basket-lift experiment](https://chorus-model.github.io/#real-world-tasks)

## Slide 09 - Robotics spans five research directions in this sample

**This table puts the two axes together.** Each row is a study’s main research direction, and each column is a domain where it was evaluated. The largest cell in each column shows which challenge received most attention in that domain in our sample. In software, 23 of 37 studies focus on adaptation. Think of a failed test or a change that breaks another agent’s work. The team may have to repair, reassign, or replan. In agent economies, 37 of 39 focus on trust and incentives. Buyers and sellers may have different objectives, so what to believe and how to transact matter. In robotics, 26 of 36 focus on language-guided robotics, with the other ten covering adaptation, teaming, learning, and verification. These are counts of research topics. The next slide asks where the robotics evidence comes from.

Source details: see the slide hyperlinks and sources.json.

## Slide 10 - Simulation is more common than physical execution

**Simulation is more common than hardware execution in the robotics subset.** Twenty-six studies explicitly use simulation and ten report running on physical robots. These settings can overlap. The largest task group is manipulation, handover, and household work, with fifteen studies. Simulation lets us repeat conditions. On hardware, a robot must keep its grip and clearances while its partner moves. That describes the coordination papers we reviewed. How visible is the topic when we look at four major robotics conferences?

Source details: see the slide hyperlinks and sources.json.

## Slide 11 - Multi-robot coordination appears in 49 per 1,000 titles

**Multi-robot coordination appears in about 49 of every thousand titles across the four robotics venues.** For comparison, planning and control appear in 197 per thousand, and manipulation and grasping in 160. I’ve pooled the four 2026 programs, so each bar has the same denominator. The topics can overlap. A coordinated motion-planning paper can contribute to both bars. Now think about what a robot has to do on its own. Opening a door it hasn’t seen means handling a new shape and a different hinge or mechanism. HiFun’s tool-retrieval example shows another issue. If the fingertips slip, the robot has to restore contact and adjust the force before it can continue. These capabilities are useful with one robot and still matter in a team. When two robots carry a basket, a stable grasp is only part of the job. In CHORUS, one carrier has to pause while the other adjusts to clear the doorframe, otherwise the basket can slip. That dependence on a teammate’s action is what coordination has to manage. It also changes the data we need if we learn from demonstrations, because the training examples have to capture how their actions fit together. The chart tells us how often these topics appear in the programs. The next two applications show when that extra work pays off.

Sources: [GRACE paper](https://arxiv.org/abs/2603.10858) · [Roken paper](https://arxiv.org/abs/2606.15550) · [Roken on the CoRL program](https://openreview.net/forum?id=4ar3F6Obiq) · [RSS 2026 program](https://roboticsconference.org/2026/program/papers/) · [ICRA 2026 program](https://ras.papercept.net/conferences/conferences/ICRA26/program/) · [IROS 2026 index](https://2026.ieee-iros.org/program/paper_index/) · [CoRL 2026 papers](https://2026.corl.org/program/accepted-papers) · [CoRL 2026 · HiFun](https://hly-123.github.io/HiFun/) · [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1) · [RSS 2025 · ArticuBot](https://roboticsconference.org/2025/program/papers/156/)

## Slide 12 - Coordination protects flow and makes joint work possible

**Coordination creates two different kinds of value in these applications.** In a warehouse it protects flow. Several robots need the same aisles, so timing and access determine whether they keep moving or wait for each other. In manipulation it makes a joint task possible. Roles and handoffs have to fit, or one robot can act before its teammate is ready. I’ll show one case for each and distinguish the example from the measurement that supports it.

Sources: [Amazon · DeepFleet](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model) · [Tan et al. · CREST](https://arxiv.org/html/2603.28803) · [Google DeepMind · ER 2](https://deepmind.google/models/gemini-robotics/embodied-reasoning/) · [DuoMind · Figure 4a](https://arxiv.org/html/2610.02161v1#S4.SS3)

## Slide 13 - Coordinating warehouse traffic reduces blocking

**Fleet coordination reduces avoidable waiting and blocking.** The Amazon example shows why it matters at scale. Amazon reported one million robots across its network when it introduced DeepFleet, and projected a ten percent improvement in travel efficiency. For a controlled number, look at the separate CREST warehouse benchmark. On the hundred-agent staging-to-warehouse layout, CREST kept the same shelf plan and adjusted how robots carried it out. It cut normalized makespan by 23.5 percent versus MAPF-DECOMP. That metric subtracts a reference term from the time to finish. The result quantifies execution on that benchmark. Now let’s move from coordinating routes to coordinating a shared action.

Sources: [Amazon · DeepFleet](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model) · [Tan et al. · CREST](https://arxiv.org/html/2603.28803)

## Slide 14 - Coordination aligns roles and handoffs

**Coordination makes a handoff succeed by aligning who acts and when.** The Gemini demo illustrates delegation by capability. For a measured effect, DuoMind uses the same system with peer messages enabled or disabled. Across seven simulated RoboPoly tasks, mean success is 35.75 percent with messages and 26.25 without them. In Cook Pot it’s 39.25 versus one percent. The authors observed that without messages, one robot sometimes started lifting while its teammate was still grasping. That connects the number to a mechanism. A message can carry readiness the other robot can’t see.

Sources: [Google DeepMind · ER 2](https://deepmind.google/models/gemini-robotics/embodied-reasoning/) · [Gemini ER 2 model card](https://deepmind.google/models/model-cards/gemini-robotics-er-2/) · [DuoMind · Figure 4a](https://arxiv.org/html/2610.02161v1#S4.SS3)

## Slide 15 - Fleet operators, labs and standards groups tackle coordination

**The different communities solve different dependencies.** Amazon focuses on moving fleets through shared space. Stanford’s CHORUS focuses on robots reacting to teammates during a physical task. Open-RMF and standards groups address how independent fleets share a building. The horizontal axis describes how public each linked contribution is, from deployed products to papers and open artifacts. Across those systems, a useful comparison is who has the authority to change a shared decision during execution.

Sources: [Announcement](https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model) · [Demo](https://deepmind.google/models/gemini-robotics/embodied-reasoning/) · [Technical article](https://www.intrinsic.ai/blog/posts/specialized-ai-for-scalable-and-adaptive-multi-robot-orchestration) · [Project](https://rsl.ethz.ch/research/challenges-competitions/cerberus.html) · [RSS 2026](https://www.roboticsproceedings.org/rss22/p036.html) · [Project](https://hanchuzhou.github.io/duomind_project_page/) · [Project](https://chorus-model.github.io/) · [Paper](https://arxiv.org/html/2607.12050v1) · [Project](https://sites.google.com/view/smart-llm/) · [Documentation](https://docs.isaacsim.omniverse.nvidia.com/latest/ros2_tutorials/robot_control/tutorial_ros2_multi_navigation.html) · [Demo](https://github.com/open-rmf/rmf_demos) · [Source code](https://github.com/proroklab/magat_pathplanning) · [Benchmark](https://aihabitat.org/partnr/) · [Specification](https://github.com/VDA5050/VDA5050) · [Specification](https://github.com/MassRobotics-AMR/AMR_Interop_Standard)

## Slide 16 - Robot architectures differ in who can change the plan

**The architectural difference is who can revise a shared action at runtime.** A centralized planner makes that decision at team level. A hybrid design gives robots some local decision authority and keeps other decisions at team level. In a decentralized design, robots decide locally and coordinate through cues, messages, or protocols. Of the 25 studies with a classified architecture, eleven are centralized, five are hybrid, and nine are decentralized. CHORUS makes the distinction concrete. The robots share trained weights, while each robot makes its own runtime decisions. That architectural choice tells us who acts. To see why the architectures differ, let’s look at the operating conditions that shaped them.

Sources: [DuoMind](https://arxiv.org/html/2610.02161v1) · [Purdue SMART Lab · SMART-LLM](https://arxiv.org/html/2309.10062v2) · [EFLUX · paper](https://arxiv.org/html/2607.12050v1) · [He et al. · Closed-loop manipulation](https://www.roboticsproceedings.org/rss22/p036.html) · [Chinese Academy of Sciences · EmboTeam](https://arxiv.org/html/2601.11063) · [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1) · [Meta FAIR · PARTNR](https://aihabitat.org/partnr/)

## Slide 17 - Three changes drove new coordination questions

**Three changes made different coordination questions important.** First, field robots faced incomplete maps and weak links, so local autonomy mattered alongside team-level plans. Second, language models made it practical to turn an open-ended instruction into proposed roles and actions. A motion planner still had to verify that the proposal was physically possible. Third, a demo on a few tasks couldn’t tell us how broadly a method works. Larger benchmarks expanded task coverage, while hardware tests exposed contact and timing. Those are the drivers I’ll use to read the timeline.

Sources: [Li et al. · Lifelong MAPF](https://arxiv.org/abs/2005.07371) · [Tranzatto et al. · CERBERUS](https://arxiv.org/abs/2207.04914) · [Mandi et al. · RoCo](https://ieeexplore.ieee.org/document/10610855) · [PARTNR paper](https://arxiv.org/abs/2411.00081) · [Stanford · CHORUS demos](https://chorus-model.github.io/)

## Slide 18 - From assigning jobs to adapting robot teams

**Each milestone answers a different question left open by the setting before it.** Assigning jobs gives robots destinations, which creates a routing problem. Lifelong routing handles arrivals on a known map. CERBERUS asks how to keep working with weak links and incomplete maps. RoCo uses LLM dialogue when robots need to agree on roles and actions from a task description. PARTNR asks whether planners handle many more kinds of dependencies, and CHORUS takes a specific dependency back to hardware. These directions develop in parallel. Let’s start with what warehouse routing already handles well.

Sources: [Gerkey & Matarić · MRTA](https://robotics.usc.edu/publications/media/uploads/pubs/347.pdf) · [Wurman et al. · Kiva](https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v29i1.2082) · [Li et al. · Lifelong MAPF](https://arxiv.org/abs/2005.07371) · [Tranzatto et al. · CERBERUS](https://arxiv.org/abs/2207.04914) · [Mandi et al. · RoCo](https://ieeexplore.ieee.org/document/10610855) · [PARTNR · ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3cf318fbeec1126da21e9185ae9908c-Abstract-Conference.html) · [Stanford · CHORUS demos](https://chorus-model.github.io/)

## Slide 19 - Classical routing handled 1,000 agents in simulation

**Classical routing is a strong baseline when the map and goals are known.** Kiva connects assigning a job with getting the robot to the right place. Lifelong MAPF handles continuing arrivals by resolving conflicts in a short time window, then shifting the window as new goals come in. That makes the paths easier to update. The authors tested up to a thousand agents in simulated warehouses. The next constraint is what happens when the team must discover the map and can’t rely on a stable link.

Sources: [MRTA](https://robotics.usc.edu/publications/media/uploads/pubs/347.pdf) · [Kiva](https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v29i1.2082) · [Lifelong MAPF](https://arxiv.org/abs/2005.07371)

## Slide 20 - CERBERUS kept robots operating with limited communication

**CERBERUS shows why some decisions must stay onboard when communication is limited.** The legged and aerial robots could navigate and map underground without GPS, while the team reported what it found at mission level. That division let local exploration continue when links were poor. It won the 2021 DARPA final systems competition. The field result covers exploration, mapping, and reporting. A shared manipulation task introduces a different dependency. Robots have to agree on who handles the object and when to hand it over.

Sources: [Báo cáo CERBERUS](https://arxiv.org/abs/2207.04914) · [ETH Zürich · demo](https://rsl.ethz.ch/research/challenges-competitions/cerberus.html)

## Slide 21 - RoCo pairs dialogue with motion checks

**LLMs gave robots a way to propose roles and handoffs from language.** RoCo makes that useful by pairing dialogue with a motion planner and environment feedback. A verbal plan can say who hands over the object. The motion check asks whether both robots can reach the handoff and move without conflict. RoCoBench has six task types, which lets us study that mechanism in a focused setting. The next question is how broadly it works across spatial, timing, and capability constraints. PARTNR provides that wider test coverage.

Sources: [Paper RoCo](https://ieeexplore.ieee.org/document/10610855) · [Hình và demo](https://project-roco.github.io/)

## Slide 22 - PARTNR makes coordination failures visible at scale

**PARTNR makes it possible to test a wider range of coordination failures.** Its hundred thousand tasks run in Habitat and vary where an action happens, which step comes first, and what each partner can do. In the cup example, the agents have to bring the cups to the kitchen, fill them, and then take them to the dining table. That sequence lets us see whether the team tracks progress and recovers from a mistake. The breadth is in simulation. Contact and physical recovery are questions for hardware tests. That brings us to the different kinds of evidence behind current systems.

Sources: [PARTNR · benchmark, data và code](https://aihabitat.org/partnr/) · [Paper](https://arxiv.org/abs/2411.00081) · [PARTNR · ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3cf318fbeec1126da21e9185ae9908c-Abstract-Conference.html)

## Slide 23 - How we select works for the Current Frontier

**I start with a simple test for a hard problem.** What would make this team fail even if each robot could do its own part? Paths might collide, two actions might fall out of sync, one robot might lack information about the other, or a new teammate might behave differently. Once we know what breaks, we can judge whether the paper offers an idea we could use, compares it against strong baselines, and tests it as the team or workload grows. The research groups tell us who is developing the ideas. The experiments tell us what those ideas can do. Let’s put one main example next to each problem.

Sources: [RoboBallet · paper and videos](https://arxiv.org/html/2509.05397v1) · [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1) · [EFLUX · paper](https://arxiv.org/html/2607.12050v1) · [DuoMind · paper](https://arxiv.org/html/2610.02161v1) · [RoboTalk · paper](https://arxiv.org/html/2609.23997v2) · [HOLA · open adaptive teaming](https://arxiv.org/html/2607.04972v1)

## Slide 24 - Four problems can stop a robot team

**This table separates what makes coordination hard from who decides what to do.** In RoboBallet, arm paths can collide, so one planner uses the workcell state and issues commands for all arms. In CHORUS, two robots can lose timing during a handoff. Each runs its own copy of the same VLA and reacts to what it sees, without messages. RoboTalk also leaves the decision with each robot, but adds messages when a peer’s progress is hidden. HOLA uses local policies and asks whether they still cooperate when the partners or team size change. The last column shows what was actually tested. RoboBallet varies arm count in simulation and separately runs on four real arms. RoboTalk evaluates two robots in simulation. Let’s start with the centralized case, then compare what changes when a robot has to decide for itself.

Sources: [RoboBallet · paper and videos](https://arxiv.org/html/2509.05397v1) · [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1) · [RoboTalk · paper](https://arxiv.org/html/2609.23997v2) · [HOLA · open adaptive teaming](https://arxiv.org/html/2607.04972v1)

## Slide 25 - RoboBallet plans tasks and motions jointly for robot arms

**RoboBallet learns to plan assignments and movements jointly because one arm’s path changes what others can do.** It represents arms, targets, and obstacles as a graph. During reinforcement learning, simulated workcells vary robot positions, obstacles, and target poses, so the policy sees many combinations of those constraints. The scale experiment is eight arms and forty targets in simulation. A separate four-arm model trained with the same framework produces trajectories executed on physical robots. CHORUS changes where the decision lives. Each robot acts from its own view.

Sources: [RoboBallet · Results và Movie 2](https://arxiv.org/html/2509.05397v1) · [Science Robotics](https://doi.org/10.1126/scirobotics.ads1204) · [Intrinsic · Multi-robot orchestration](https://www.intrinsic.ai/blog/posts/specialized-ai-for-scalable-and-adaptive-multi-robot-orchestration)

## Slide 26 - RoboBallet learns one joint action for the workcell

**RoboBallet turns assignment, scheduling, and motion planning into one control problem.** The state graph contains the arms, the remaining targets, and the obstacles. One forward pass outputs the joint velocities for every arm. Assignment emerges from which arm reaches which target. In the reward, S is the fraction of completed targets, so a newly reached target gives positive credit. A proposed collision adds a penalty. The simulator blocks the unsafe motion. The authors randomize the workcell, collect rollouts, and use hindsight replay to relabel some missed targets to poses the arms actually visited. Modified TD3 then trains one deterministic graph actor and two graph critics from replay. The next question is how much trajectory quality that learning procedure gives up.

Sources: [RoboBallet · paper and videos](https://arxiv.org/html/2509.05397v1)

## Slide 27 - RoboBallet approaches the exhaustive baseline’s trajectory cost

**RoboBallet gets close to the exhaustive reference on the simplified comparison.** The authors use ten sets of twenty reaching targets. Each target can be reached by only one arm, so this test removes the assignment choice. The RRT-Connect references plan each arm separately, either with a random schedule or with exhaustive schedules and up to eight inverse-kinematics samples per target. RoboBallet’s completion times are comparable to the strongest of those references. Keep the conditions in view. RRT-Connect solves exact poses in isolation, while RoboBallet accepts a pose tolerance and checks collisions across arms. The eight-arm, forty-target simulation runs at about 0.3 milliseconds of planning per step on an A100. Four-arm hardware execution is a separate demonstration. Next we’ll look at a system in which each robot generates its own actions.

Sources: [RoboBallet · paper and videos](https://arxiv.org/html/2509.05397v1) · [RoboBallet · Science Robotics](https://doi.org/10.1126/scirobotics.ads1204)

## Slide 28 - CHORUS trains one policy and runs it locally on each robot

**CHORUS learns one shared policy from joint demonstrations, then runs it independently on each robot.** The training data show what each robot sees and does during coordinated tasks. A robot-identifying prompt tells the pretrained vision-language-action model which embodiment it controls. At runtime, each copy uses local observations to infer timing from its teammate’s visible behavior. That gives us a testable claim. Can local visual cues support the basket task on physical robots?

Sources: [CHORUS · architecture and paper](https://chorus-model.github.io/) · [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1)

## Slide 29 - CHORUS fits one flow-matching policy to every robot’s view

**CHORUS trains one VLA on all robots’ views of the same demonstrations.** For robot r, o is its local camera and proprioception input, c is its identity and role prompt, and A is a short sequence of its actions. Training samples those tuples from the pooled demonstrations. In the lower equation, a random mix of noise and the demonstrated actions gives a noised chunk. The model predicts the vector field that connects noise and actions, and the squared error supplies the training signal. The authors fine-tune the pretrained pi-zero-point-five backbone with LoRA and AdamW. At deployment every robot uses the same weights, its own views, and its own control timing. The next experiment tests which of those design choices actually helps.

Sources: [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1) · [Stanford · CHORUS demos](https://chorus-model.github.io/)

## Slide 30 - Shared weights help CHORUS recover a perturbed handover

**The strongest test of shared weights is what happens when a teammate moves unexpectedly.** First, the plot compares three physical tasks, basket lifting, tape measurement, and book handover. The full method gains 64 percentage points in mean task success over decentralized diffusion trained from scratch. The paper also trains a centralized VLA that sees both robots and outputs both action chunks. CHORUS matches or exceeds that baseline on these three tasks. Finally, hold the pretrained backbone fixed and perturb the robot offering a book. With separate policies, the receiver completes nine of twenty handovers. With shared weights, it completes seventeen. That last comparison is the evidence for reactivity under this perturbation. Next we’ll see what a third robot changes.

Sources: [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1) · [Stanford · CHORUS demos](https://chorus-model.github.io/)

## Slide 31 - CHORUS reached 90% on one three-robot transport task

**CHORUS reached ninety percent success on this three-robot transport task.** Two robots carry the basket and one handles the door. One carrier can’t see the door behind it, but can infer when to proceed from its teammate’s movement. The team was trained for this task, and the relevant visual cue was available. What if the robot can’t see whether its teammate has finished a step? That’s the setting where RoboTalk studies when to send a message and when to act.

Sources: [CHORUS · Scaling to three robots và demo](https://chorus-model.github.io/) · [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1)

## Slide 32 - RoboTalk learns messages and tool calls from the same traces

**RoboTalk moves the learning target up from motor commands to skill and communication choices.** Each robot sees a local history and predicts the next tool call. A call can send a message, wait for a signal, navigate, or invoke manipulation. The objective rewards high probability on the demonstrated output tokens. To build those targets, Gemini generates joint traces with a leader-follower protocol and explicit wait-and-release messages. A finite-state machine checks the preconditions and rejects invalid traces. The team replays the accepted traces in simulation for images, then fine-tunes one shared eight-billion-parameter Qwen vision-language model with LoRA. In some runs the target includes a rationale before the tool call. That gives us a specific training choice to test next.

Sources: [RoboTalk · paper](https://arxiv.org/html/2609.23997v2)

## Slide 33 - RoboTalk improves held-out tasks with supervised traces

**Supervised training makes a large difference on the held-out kitchen tasks.** A rollout counts as successful only if the team reaches the task goal without failed or rejected tool calls and within budget. With full protocol guidance, untuned Qwen Instruct scores zero percent. With the same model after fine-tuning on a hundred and fifty examples per training task, the held-out score is sixty-five percent. The figure asks a different question. At thirty demonstrations per task and within the Thinking model, adding rationale targets raises held-out success from fifty to seventy-one percent. The best run reaches seventy-seven at a different data size, so read the rationale effect from the matched pair. These are simulated skill calls. HOLA now takes us from new tasks to new teammates.

Sources: [RoboTalk · paper](https://arxiv.org/html/2609.23997v2)

## Slide 34 - New teammates and larger teams require separate tests

**HOLA trains for changes in who is on the team, where they work, and how large the team is.** The hypergraphic game represents dependencies across groups of robots. Its open-ended training increases the diversity of partners and environments the policy encounters. Evaluation separates unseen partners, new layouts, and team size. The physical transfer is in cooperative pursuit on drones and quadrupeds. That takes us back to the timeline question. What kind of adaptation has actually been tested, and what changes still need a controlled experiment?

Sources: [HOLA · §§V–VI và Figure 4](https://arxiv.org/html/2607.04972v1)

## Slide 35 - HOLA trains against a changing population of teammates

**HOLA changes who the learner trains with.** The objective averages the pursuit reward over teammates, layouts, and active team compositions. A successful team gains reward for capture and faces penalties for constraint violations. The algorithm first seeds a diverse population with a reward-and-entropy objective. Then the Grapher scores groups of policies that play together and stores their returns on hyperedges. The Oracle uses marginal coalition value to sample weaker partners more often, as shown by the reciprocal in the second equation. It trains an approximate best response against those teams and adds the new policies to the population. That gives us two different things to test. Can the learner handle partners it hasn’t met, and can it still adapt when the map or the team changes?

Sources: [HOLA · open adaptive teaming](https://arxiv.org/html/2607.04972v1)

## Slide 36 - HOLA’s gains depend on which generalization is tested

**HOLA’s advantage depends on what is held out.** In the first pursuit test, the team stays fixed within an episode, but the learner gets unfamiliar partners. The plot shows eighty-two percent capture for HOLA and seventy-two for Fictitious Co-Play. The authors also compare MAPPO and DACOOP-A in the text, and neither exceeds forty percent in this setting. When the partners and the layouts both change, the numbers are much closer. HOLA reaches forty-four percent and population-based training reaches 42.67 percent. The paper separately tests open teams, where robots can join or leave mid-episode, and shows physical drone and quadruped deployments. In the separate open-team quadruped test on unseen maps, HOLA reaches 62.6 percent capture, about six points above MAPPO. The combination of tests matters because adapting to a teammate and adapting to a new environment are different capabilities.

Sources: [HOLA · open adaptive teaming](https://arxiv.org/html/2607.04972v1)

## Slide 37 - Current results point to three tests of adaptation

**Current systems give us three concrete questions about adaptation.** Historically, the field moved from assigning and routing robots to specifying collaboration and testing it across tasks. Today we have joint motion planning in RoboBallet, local visual handoffs in CHORUS, and cross-vendor routing in RoMi-H. Now look at the three signals below. He and colleagues use verification feedback to replan on hardware. Li and colleagues show agents recruiting help after a refusal in simulation. And ISO 21423 defines how fleets and infrastructure communicate. These motivate three tests. Can a team repair a failed handoff locally? Can it work with an unfamiliar partner? Can independent fleets resolve contention over an aisle? The next slide shows how we could test each one.

Sources: [He et al. · Closed-loop manipulation](https://www.roboticsproceedings.org/rss22/p036.html) · [Li et al. · Nature Communications](https://pmc.ncbi.nlm.nih.gov/articles/PMC13376541/) · [ISO 21423:2026](https://www.iso.org/standard/86749.html) · [RoboBallet · paper and videos](https://arxiv.org/html/2509.05397v1) · [Stanford · CHORUS demos](https://chorus-model.github.io/) · [Changi General Hospital · RoMi-H](https://www.cgh.com.sg/about-cgh/news/caring/issue4-2022/driving-automation-in-and-beyond-healthcare) · [Gerkey & Matarić · MRTA](https://robotics.usc.edu/publications/media/uploads/pubs/347.pdf) · [Wurman et al. · Kiva](https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v29i1.2082) · [Mandi et al. · RoCo](https://ieeexplore.ieee.org/document/10610855) · [PARTNR · ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3cf318fbeec1126da21e9185ae9908c-Abstract-Conference.html) · [He et al. · Author affiliations](https://arxiv.org/html/2607.06990v1)

## Slide 38 - Three experiments can test whether robot teams adapt

**Each experiment changes one condition and measures what the whole team does next.** In the figure, He and colleagues report 63 percent average final success across three tabletop tasks with disturbances. That tells us how often their full recovery loop finished the task. Our first proposed test injects the same handoff failure in RoCoBench and repeats selected cases on hardware. Compare a fixed plan, a full replan, and local repair. The second holds out a teammate in a RoboPoly-style task and compares local cues with selective messages. The third gives independent fleets competing routes in Open-RMF and compares a central scheduler with reservations. Success, recovery time, communication cost, throughput, and deadlocks tell us where each approach helps. Together the tests ask which decisions a robot can handle locally and which ones need a shared rule.

Sources: [He et al. · Closed-loop manipulation](https://www.roboticsproceedings.org/rss22/p036.html) · [RoCo project and demos](https://project-roco.github.io/) · [DuoMind · paper](https://arxiv.org/html/2610.02161v1) · [Open Robotics · Open-RMF demos](https://github.com/open-rmf/rmf_demos) · [HOLA · open adaptive teaming](https://arxiv.org/html/2607.04972v1)

## Slide 39 - Decide what stays local and what the team must share

**The goal is to keep the team working safely when its plan changes.** In the basket example, a robot should be able to pause or stabilize the load locally. Starting the lift depends on both robots, so that decision has to be coordinated. We can compare designs under the same disruption by measuring safe completion, recovery time, and communication cost. That brings us back to the question at the bottom. When the original plan breaks, can the team still finish the shared job safely?

Sources: [RoboBallet · Science Robotics](https://doi.org/10.1126/scirobotics.ads1204) · [Stanford · CHORUS demos](https://chorus-model.github.io/) · [Changi General Hospital · RoMi-H](https://www.cgh.com.sg/about-cgh/news/caring/issue4-2022/driving-automation-in-and-beyond-healthcare) · [He et al. · Closed-loop manipulation](https://www.roboticsproceedings.org/rss22/p036.html)

## Slide 40 - What to read for each coordination problem

**Pick a reading path based on what you want your robots to do.** For motion, compare Lifelong MAPF’s rolling-horizon planner with RoboBallet’s learned policy. For handoffs, read CHORUS for local visual cues and He and colleagues for verification and recovery. If the issue is what robots know about each other, start with RoCo for dialogue, then compare DuoMind’s prompted messages with RoboTalk’s learned ones. If partners or plans can change, HOLA, Proactive Collaboration, and EmboTeam show different ways to handle that. PARTNR and TeamCraft are simulation resources. Kiva, RoMi-H, and ISO 21423 explain what fleet deployment and interoperability require.

Sources: [Li et al. · Lifelong MAPF](https://arxiv.org/abs/2005.07371) · [RoboBallet · paper and videos](https://arxiv.org/html/2509.05397v1) · [EFLUX · paper](https://arxiv.org/html/2607.12050v1) · [RSS 2025 · APEX-MR](https://roboticsconference.org/2025/program/papers/98/) · [Doshi et al. · CHORUS](https://arxiv.org/html/2606.12352v1) · [He et al. · Closed-loop manipulation](https://www.roboticsproceedings.org/rss22/p036.html) · [RoCo project and demos](https://project-roco.github.io/) · [DuoMind · paper](https://arxiv.org/html/2610.02161v1) · [RoboTalk · paper](https://arxiv.org/html/2609.23997v2) · [HOLA · open adaptive teaming](https://arxiv.org/html/2607.04972v1) · [Li et al. · Nature Communications](https://pmc.ncbi.nlm.nih.gov/articles/PMC13376541/) · [Chinese Academy of Sciences · EmboTeam](https://arxiv.org/html/2601.11063) · [PARTNR · ICLR 2025](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3cf318fbeec1126da21e9185ae9908c-Abstract-Conference.html) · [TeamCraft · 2024 arXiv preprint](https://arxiv.org/abs/2412.05255) · [Wurman et al. · Kiva](https://onlinelibrary.wiley.com/doi/abs/10.1609/aimag.v29i1.2082) · [Changi General Hospital · RoMi-H](https://www.cgh.com.sg/about-cgh/news/caring/issue4-2022/driving-automation-in-and-beyond-healthcare) · [ISO 21423:2026](https://www.iso.org/standard/86749.html)

## Slide 41 - Two other ways to solve the same coordination problems

**The appendix compares two alternatives to the main examples.** EFLUX also handles space, but it changes the shape of a moving formation to get through a bottleneck. It plans the waypoints for the whole team, then uses distributed tracking in simulation. DuoMind also handles information gaps. Each robot has its own prompted orchestrator for messages and subtasks and a separate action model for execution. The next slides show these two designs in detail.

Sources: [EFLUX · paper](https://arxiv.org/html/2607.12050v1) · [DuoMind · paper](https://arxiv.org/html/2610.02161v1) · [RoboBallet · paper and videos](https://arxiv.org/html/2509.05397v1) · [RoboTalk · paper](https://arxiv.org/html/2609.23997v2)

## Slide 42 - EFLUX uses geometry to reshape or split robot teams

**EFLUX handles the same broad spatial dependency as RoboBallet, but changes what the team must decide.** Here the robots must fit through a narrow passage as a group. The system turns the map and nominal formation into a geometric description of the bottleneck. An LLM proposes whether to reshape the formation or split it and merge later. The system then checks and corrects the robot waypoints. The next slide shows what this buys on a narrow-gap test and how performance changes with more robots.

Sources: [EFLUX](https://arxiv.org/html/2607.12050v1) · [TeamingLTL](https://roboticsproceedings.org/rss22/p035.html) · [Connectivity maintenance](https://roboticsproceedings.org/rss22/p043.html)

## Slide 43 - EFLUX traverses a narrow gap more reliably

**EFLUX succeeds more often in the narrow-passage test, while SF traverses it faster on successful runs.** For the square formation, EFLUX succeeds in all twenty runs and SF in eighteen. In a separate scaling experiment, EFLUX succeeds in every run with four and six robots and in sixty percent with eight, with the formation footprint held fixed. This result makes a useful comparison with RoboBallet. Both test increasing robot counts, under different geometric and task constraints.

Sources: [EFLUX · paper](https://arxiv.org/html/2607.12050v1)

## Slide 44 - Messages help when teammates cannot see the same state

**DuoMind gives us a second way to handle the information problem we saw in RoboTalk.** Each robot uses a prompted vision-language model to decide what to say and what subtask to run. A separate action model executes the subtask, and that model is fine-tuned on robot demonstrations. RoboTalk fine-tunes the model that chooses both messages and skill calls. That difference lets us compare a prompted communication layer with one learned from traces, while keeping in mind that the papers use different tasks.

Sources: [DuoMind](https://arxiv.org/html/2610.02161v1) · [RoboTalk](https://arxiv.org/html/2609.23997v2)

## Slide 45 - DuoMind prompts the planner and fine-tunes the controller

**DuoMind learns motor execution and uses a prompted model to decide what to do and say.** Robot i’s Qwen orchestrator receives the global task, its observations, and incoming messages. It emits a local subtask and a message for peers. The pi-zero-point-five controller conditions on the subtask and observations and produces an action chunk. For RoboPoly, the authors script key states and use a motion planner to generate joint demonstrations, then replay them to record camera observations. The local command and demonstrated actions supervise LoRA fine-tuning of the VLA. On RoboTwin the training labels provide the high-level goal, although evaluation still passes decomposed commands to the controller. That distinction matters when we interpret the benchmark numbers.

Sources: [DuoMind · paper](https://arxiv.org/html/2610.02161v1)

## Slide 46 - DuoMind’s gains vary by task

**DuoMind shows a large gain on some tasks and a small loss on one of the examples here.** The experiments cover seven RoboPoly tasks and eight RoboTwin tasks, with four hundred simulated rollouts per task and method. The standalone pi-zero-point-five and pi-zero baselines are also fine-tuned, but receive the high-level goal directly. On Cook Pot, DuoMind reaches 39.25 percent and the standalone pi-zero-point-five reaches one percent. For Put Object Cabinet in RoboTwin, that same standalone controller does a little better. To isolate communication, keep DuoMind and switch off incoming peer messages. The RoboPoly mean falls from 35.75 to 26.25 percent. That ablation is the comparison that tells us what the messages add.

Sources: [DuoMind · paper](https://arxiv.org/html/2610.02161v1) · [DuoMind · Figure 4a](https://arxiv.org/html/2610.02161v1#S4.SS3)
