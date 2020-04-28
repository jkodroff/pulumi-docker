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
    public sealed class ContainerVolume
    {
        /// <summary>
        /// The path in the container where the
        /// device will be binded.
        /// </summary>
        public readonly string? ContainerPath;
        /// <summary>
        /// The container where the volume is
        /// coming from.
        /// </summary>
        public readonly string? FromContainer;
        /// <summary>
        /// The path on the host where the device
        /// is located.
        /// </summary>
        public readonly string? HostPath;
        /// <summary>
        /// If true, this volume will be readonly.
        /// Defaults to false.
        /// </summary>
        public readonly bool? ReadOnly;
        /// <summary>
        /// The name of the docker volume which
        /// should be mounted.
        /// </summary>
        public readonly string? VolumeName;

        [OutputConstructor]
        private ContainerVolume(
            string? containerPath,

            string? fromContainer,

            string? hostPath,

            bool? readOnly,

            string? volumeName)
        {
            ContainerPath = containerPath;
            FromContainer = fromContainer;
            HostPath = hostPath;
            ReadOnly = readOnly;
            VolumeName = volumeName;
        }
    }
}