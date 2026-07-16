# Professions coverage map

The atlas has two kinds of jobs:

1. **Task jobs** (the original ~200): "I'm about to do X task" — pdf-generation, postgresql-database, react-development.
2. **Profession jobs** (this layer): "I do X for a living — which skills make an agent useful to me?" — accountant, lawyer, marketer.

Profession files live in `jobs/` like any other job, follow the same schema and trust
tiers, and lean heavily on **cross-references into task jobs** (an accountant file points
at office-documents, pdf-generation, data-validation-quality rather than re-listing them).

**Honesty rule applies with extra force here:** many professions have a thin/empty public
skill layer. The correct entry for those is a short honest file that says so and points to
the nearest tooling + what to fork private — NOT padded Tier-C junk. A thin file is a
finding, not a failure.

Target: cover the online-doable professions (SOC-inspired taxonomy below, ~260). Combined
with the ~200 task jobs this lands the atlas around ~460–500 total, grown in verified
batches — never by padding.

Status legend: ✅ = job file exists · (w1)…(wN) = planned wave · blank = backlog.

## Business & Management
- ✅ project-manager (w1)
- product-manager
- program-manager
- operations-manager
- business-analyst
- management-consultant
- scrum-master
- agile-coach
- chief-of-staff
- strategy-analyst
- hr-manager
- hr-generalist
- ✅ recruiter-talent-acquisition (w1)
- compensation-benefits-analyst
- learning-development-specialist
- compliance-officer
- procurement-specialist
- supply-chain-analyst
- logistics-coordinator
- real-estate-agent
- property-manager
- fundraiser-grant-manager
- nonprofit-program-manager
- franchise-consultant
- business-broker

## Finance & Accounting
- ✅ accountant-bookkeeping (w1)
- ✅ financial-analyst (w1)
- auditor
- tax-preparer
- payroll-specialist
- accounts-payable-receivable-clerk
- financial-planner-advisor
- credit-analyst
- risk-analyst
- treasury-analyst
- insurance-underwriter
- insurance-claims-adjuster
- actuary
- investment-analyst
- equity-researcher
- trader
- portfolio-manager
- fund-administrator
- fpna-analyst
- forensic-accountant
- billing-specialist
- collections-specialist
- mortgage-loan-processor
- financial-controller

## Legal
- ✅ lawyer-legal-work (w1)
- paralegal
- contract-manager
- legal-researcher
- patent-agent
- trademark-specialist
- compliance-paralegal
- e-discovery-specialist
- legal-operations-manager
- court-transcriptionist
- immigration-consultant
- privacy-officer-dpo

## Sales & Marketing
- ✅ marketer-digital-marketing (w1)
- seo-specialist
- sem-ppc-specialist
- content-marketer
- social-media-manager
- email-marketing-specialist
- growth-marketer
- marketing-analyst
- market-researcher
- brand-manager
- pr-specialist
- communications-manager
- copywriter
- sales-development-rep
- account-executive
- account-manager
- customer-success-manager
- sales-engineer
- sales-operations-analyst
- crm-administrator
- ecommerce-manager
- marketplace-seller
- affiliate-marketer
- influencer-marketing-manager
- community-manager
- partnerships-manager
- product-marketing-manager
- demand-generation-manager

## Media, Design & Writing
- graphic-designer
- ui-ux-designer
- product-designer
- ux-researcher
- ux-writer
- illustrator
- motion-designer
- animator-2d-3d
- 3d-artist
- video-editor
- videographer-post
- photographer-photo-editor
- podcast-producer
- audio-engineer
- music-producer
- voice-over-artist
- ✅ journalist-newsroom (w1)
- news-editor
- technical-writer
- documentation-manager
- editor-proofreader
- ✅ translator-localization (w1)
- transcriptionist
- subtitler-captioner
- content-writer-blogger
- ghostwriter
- screenwriter
- novelist-author
- grant-writer
- resume-writer
- speechwriter
- game-designer
- game-writer-narrative
- creative-director
- art-director
- presentation-designer

## Education & Research
- ✅ teacher-educator (w1)
- online-tutor
- language-teacher
- instructional-designer
- curriculum-developer
- corporate-trainer
- course-creator
- academic-researcher
- research-assistant
- librarian-information-specialist
- education-administrator
- admissions-consultant
- test-prep-coach
- special-education-consultant

## Data & Science
- data-analyst
- statistician
- economist
- econometrician
- bioinformatician
- computational-biologist
- gis-analyst
- survey-researcher
- psychometrician
- epidemiologist
- clinical-data-manager
- research-scientist-computational
- science-communicator
- meteorologist-forecaster
- operations-research-analyst

## Healthcare (online-doable)
- medical-coder-biller
- medical-transcriptionist
- health-informatics-specialist
- telehealth-coordinator
- medical-writer
- pharmacovigilance-specialist
- clinical-trial-coordinator
- nutritionist-dietitian
- mental-health-counselor-tele
- health-coach
- medical-records-administrator
- utilization-review-specialist

## Engineering & Technical (non-software, online-doable)
- cad-drafter
- mechanical-design-engineer
- electrical-design-engineer
- civil-structural-drafter
- architect-building
- interior-designer
- landscape-designer
- pcb-designer
- simulation-engineer
- patent-illustrator
- bim-specialist
- quantity-surveyor-estimator

## Admin & Support
- virtual-assistant
- executive-assistant
- ✅ customer-support-agent (w1)
- technical-support-specialist
- data-entry-specialist
- office-manager
- scheduler-calendar-manager
- travel-agent-planner
- event-planner
- bookings-coordinator
- moderation-specialist
- claims-processor
- order-fulfillment-coordinator
- receptionist-remote

## Personal Services & Lifestyle (online-doable)
- life-coach
- career-coach
- fitness-coach-online
- yoga-instructor-online
- personal-stylist
- interior-decorator-econsult
- genealogist
- astrologer-tarot (thin-by-design)
- matchmaker
- pet-behavior-consultant
- financial-literacy-coach
- parenting-coach

## Software & IT (professions layer)
Most IT work is already covered by the ~200 task jobs — these profession files are thin
umbrellas that mostly cross-reference existing task jobs:
- backend-developer
- frontend-developer
- fullstack-developer
- mobile-developer
- devops-engineer
- site-reliability-engineer
- data-engineer
- data-scientist
- ml-engineer
- security-analyst
- penetration-tester
- qa-engineer
- database-administrator
- systems-administrator
- network-engineer
- cloud-architect
- solutions-architect
- it-support-helpdesk
- game-developer
- blockchain-developer
- embedded-developer
- ai-engineer
- prompt-engineer
- mlops-engineer
- platform-engineer
- developer-advocate
- engineering-manager
- cto-fractional
