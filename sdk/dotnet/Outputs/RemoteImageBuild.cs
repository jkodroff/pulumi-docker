// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Outputs
{

    [OutputType]
    public sealed class RemoteImageBuild
    {
        /// <summary>
        /// Set build-time variables
        /// </summary>
        public readonly ImmutableDictionary<string, string>? BuildArg;
        /// <summary>
        /// Name of the Dockerfile. Defaults to `Dockerfile`.
        /// </summary>
        public readonly string? Dockerfile;
        /// <summary>
        /// Always remove intermediate containers
        /// </summary>
        public readonly bool? ForceRemove;
        /// <summary>
        /// Set metadata for an image
        /// </summary>
        public readonly ImmutableDictionary<string, string>? Label;
        /// <summary>
        /// Do not use cache when building the image
        /// </summary>
        public readonly bool? NoCache;
        /// <summary>
        /// Context path
        /// </summary>
        public readonly string Path;
        /// <summary>
        /// Remove intermediate containers after a successful build. Defaults to  `true`.
        /// </summary>
        public readonly bool? Remove;
        /// <summary>
        /// Name and optionally a tag in the 'name:tag' format
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// Set the target build stage to build
        /// </summary>
        public readonly string? Target;

        [OutputConstructor]
        private RemoteImageBuild(
            ImmutableDictionary<string, string>? buildArg,

            string? dockerfile,

            bool? forceRemove,

            ImmutableDictionary<string, string>? label,

            bool? noCache,

            string path,

            bool? remove,

            ImmutableArray<string> tags,

            string? target)
        {
            BuildArg = buildArg;
            Dockerfile = dockerfile;
            ForceRemove = forceRemove;
            Label = label;
            NoCache = noCache;
            Path = path;
            Remove = remove;
            Tags = tags;
            Target = target;
        }
    }
}
