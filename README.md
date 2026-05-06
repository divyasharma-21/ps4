# Creator Content Posting Optimization System

## Team Information
- **Team Name**: Code Blooded
- **Year**: First
- **All-Female Team**: Yes

## Architecture Overview

**Instructions**: Describe your approach in 200 words or less. Address the following:

- How does your system determine the optimal posting time for content?
- What strategy do you use to select between Instagram and YouTube platforms?
- How do you balance platform activity patterns with creator-specific engagement history?
- What approach do you take to decide between immediate posting versus scheduling?
  

Our system is designed to optimize content performance by recommending the best platform and posting time based on historical and real-time engagement signals.

To determine the optimal posting time, we evaluate platform activity patterns across different time slots and select the time that maximizes combined engagement signals. Each time slot is scored using past platform activity data.

The platform selection strategy compares Instagram and YouTube by computing a performance score for each combination of platform and time. This score is derived from three factors: platform activity levels, historical engagement patterns for similar content, and creator-specific baseline engagement.

We balance platform activity and creator history by using weighted signals from both datasets. Platform activity captures general audience availability, while historical engagement reflects how similar content from the same creator performs under specific conditions.

Finally, the decision to post immediately or schedule is based on a comparison between current performance conditions and the predicted best scenario. If the predicted improvement exceeds a threshold, the content is scheduled; otherwise, it is posted immediately.

---

*Keep your description concise and focused on your core decision-making logic.*

**Note:** Please do not change the format or spelling of anything in this README. The fields are extracted using a script, so any changes to the structure or formatting may break the extraction process.
